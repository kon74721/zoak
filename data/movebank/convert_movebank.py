#!/usr/bin/env python

import os
import argparse
import csv
import json
import datetime
from collections import defaultdict

class Convert_movebank(object):
    def __init__(self, inputcsv, debug=False):
        self.inputcsv = inputcsv
        self.file_name = os.path.basename(inputcsv).replace('.csv', '')
        self.debug = debug
        self.study_name = None
        self.taxon = None
        self.individuals = defaultdict(dict) # { <individual-local-identifier>: [ point, ... ] }

    def run(self):
        self._parse_csv()
        self._fix_points()
        #for point in self.points:
        #    print(point)
        #print(self.interval)
        print(self._generate_json())

    def _parse_csv(self):
        entry_timestamp = 2
        entry_long = 3
        entry_lat = 4
        entry_taxon = None
        entry_individuallocalid = None
        entry_studyname = None
        with open(self.inputcsv, 'r') as f:
            lines = f.readlines()
            for entry in list(csv.reader(lines)):
                if entry[0] == 'event-id':
                    if 'individual-taxon-canonical-name' in entry:
                        entry_taxon = entry.index('individual-taxon-canonical-name')
                    if 'individual-local-identifier' in entry:
                        entry_individuallocalid = entry.index('individual-local-identifier')
                    if 'study-name' in entry:
                        entry_studyname = entry.index('study-name')
                    continue
                if not self.study_name and (entry_studyname and entry[entry_studyname] != ""):
                    self.study_name = entry[entry_studyname]
                if not self.taxon and (entry_taxon and entry[entry_taxon] != ""):
                    self.taxon = entry[entry_taxon]
                if entry[entry_timestamp] == "" or entry[entry_long] == "" or entry[entry_lat] == "":
                    continue # drop empty entries
                individual_name = list()
                if self.taxon:
                    individual_name.append(self.taxon)
                if entry_individuallocalid and entry[entry_individuallocalid]:
                    individual_name.append(entry[entry_individuallocalid])
                if len(individual_name) == 0:
                    individual_name.append(self.file_name)
                individual_name = ", ".join(individual_name)
                if 'points' not in self.individuals[individual_name]:
                    self.individuals[individual_name]['points'] = list()
                self.individuals[individual_name]['points'].append([ entry[entry_timestamp], float(entry[entry_long]), float(entry[entry_lat]) ])
    
    def _fix_points(self):
        for name in self.individuals:
            for point in self.individuals[name]['points']:
                point[0] = datetime.datetime.strptime(point[0][:-4], "%Y-%m-%d %H:%M:%S").isoformat()
                point.append(float(1.0)) # height
            self.individuals[name]['interval'] = ( self.individuals[name]['points'][0][0], self.individuals[name]['points'][-1][0] )

    def _generate_json(self):
        doc = list()
        doc.append({
            "id":"document",
            "version":"1.0"
        })
        for name in self.individuals:
            pkt = {
                "id": name,
                "availability": "%s/%s" % (self.individuals[name]['interval'][0], self.individuals[name]['interval'][1]),
                "billboard":{
                    "eyeOffset":{
                        "cartesian":[
                            0.0,0.0,0.0
                        ]
                    },
                    "horizontalOrigin":"CENTER",
                    "image":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAEISURBVEhLvVXBDYQwDOuojHKj8LhBbpTbpBCEkZsmIVTXq1RVQGrHiWlLmTTqPiZBlyLgy/KSZQ5JSHDQ/mCYCsC8106kDU0AdwRnvYZArWRcAl0dcYJq1hWCb3hBrumbDAVMwAC82WoRvgMnVMDBnB0nYZFTbE6BBvdUGqVqCbjBIk3PyFFR/NU7EKzru+qZsau3ryPwwCRLKYOzutZuCL6fUmWeJGzNzL/RxAMrUmASSCkkAayk2IxPlwhAAYGpsiHQjbLccfdOY5gKkCXAMi7SscAwbQpAnKyctWyUZ6z8ja3OGMepwD8asz+9FnSvbhU8uVOHFIwQsI3/p0CfhuqCSQuxLqsN6mu8SS+N42MAAAAASUVORK5CYII=",
                    "pixelOffset":{
                        "cartesian2":[
                            0.0,0.0
                        ]
                    },
                    "scale":0.8333333333333334,
                    "show":[
                    {
                        "interval": "%s/%s" % (self.individuals[name]['interval'][0], self.individuals[name]['interval'][1]),
                        "boolean": "true"
                    }
                    ],
                    "verticalOrigin":"BOTTOM"
                },
                "label": {
                    "fillColor": [ {
                        "interval": "%s/%s" % (self.individuals[name]['interval'][0], self.individuals[name]['interval'][1]),
                        "rgba":[ 255,255,0,255 ]
                    } ],
                    "font":"bold 10pt Segoe UI Semibold",
                    "horizontalOrigin":"LEFT",
                    "outlineColor":{ "rgba":[ 0,0,0,255 ] },
                    "epoch":"2012-08-04T16:00:00Z",
                    "pixelOffset":{
                        "cartesian2":[
                            10.0,0.0
                        ]
                    },
                    "scale":1.0,
                    "show":[ {
                        "interval": "%s/%s" % (self.individuals[name]['interval'][0], self.individuals[name]['interval'][1]),
                        "boolean": "true"
                    } ],
                    "style":"FILL",
                    "text": name,
                    "verticalOrigin":"CENTER"
                },
                "path":{
                    "material":{
                        "solidColor":{
                            "color":{
                                "rgba":[ 0,255,255,200 ]
                            }
                        }
                    },
                    "width": 1.0,
                    "leadTime" : 1,
                    "trailTime": 10000000,
                },
                "position":{
                    "interpolationAlgorithm":"LAGRANGE",
                    "interpolationDegree":1,
                    "cartographicDegrees": [item for sublist in self.individuals[name]['points'] for item in sublist]
                }
            }
            doc.append(pkt)

        comment = list()
        if self.taxon: comment.append(self.taxon)
        if self.study_name: comment.append(self.study_name)
        if len(comment) == 0: comment.append(self.file_name)
        comment.append('movebank')

        res = "// zoak: %s\n" % ', '.join(comment)
        res += json.dumps(doc)
        return res

if __name__ == '__main__':
    epilog = """Output is written to stdout.
    
Movebank map: https://www.movebank.org/movebank/
Movebank API documentation: https://github.com/movebank/movebank-api-doc/blob/master/movebank-api.md
"""
    parser = argparse.ArgumentParser(description='Movebank.org CSV to CZML converter', epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-d', action='store_true', dest='debug', help='Debug mode')
    parser.add_argument('inputcsv', help='Movebank CSV file')
    args = parser.parse_args()

    conv = Convert_movebank(args.inputcsv, args.debug)
    conv.run()
