require('cesium/Source/Widgets/widgets.css');
var BuildModuleUrl = require('cesium/Source/Core/buildModuleUrl');
BuildModuleUrl.setBaseUrl('./');

var _data = require('../data/index.js');

define([
'cesium/Source/Core/defined',
'cesium/Source/Core/formatError',
'cesium/Source/Core/objectToQuery',
'cesium/Source/Core/queryToObject',
'cesium/Source/Core/Cartesian2',
'cesium/Source/Core/Cartesian3',
'cesium/Source/Core/Color',
'cesium/Source/Core/Math',
'cesium/Source/DataSources/CzmlDataSource',
'cesium/Source/DataSources/GeoJsonDataSource',
'cesium/Source/DataSources/KmlDataSource',
'cesium/Source/Scene/createTileMapServiceImageryProvider',
'cesium/Source/Scene/LabelStyle',
'cesium/Source/Scene/VerticalOrigin',
'cesium/Source/Widgets/Viewer/Viewer',
'cesium/Source/Widgets/Viewer/viewerCesiumInspectorMixin',
'cesium/Source/Widgets/Viewer/viewerDragDropMixin',
], function(
defined,
formatError,
objectToQuery,
queryToObject,
Cartesian2,
Cartesian3,
Color,
CesiumMath,
CzmlDataSource,
GeoJsonDataSource,
KmlDataSource,
createTileMapServiceImageryProvider,
LabelStyle,
VerticalOrigin,
Viewer,
viewerCesiumInspectorMixin,
viewerDragDropMixin) {
'use strict';

	function init_cesium() {
		viewer = new Viewer('cesiumContainer');

	}

	function init_ui() {
		for (var name in _data) {
			var description = _data[name];
			var button = document.createElement('button');
			button.type = 'button';
			button.className = 'cesium-button';
			button.onclick = function(name) { return function() {
				viewer.dataSources.removeAll();
				viewer.dataSources.add(CzmlDataSource.load('data/'+name+'.czml'));
				viewer.zoomTo(viewer.entities);
			} }(name);
			button.textContent = name;
			document.getElementById('toolbar').appendChild(button);
		}
	}

	function test_point() {
		var citizensBankPark = viewer.entities.add({
			name : 'Zoakinoula',
			position : Cartesian3.fromDegrees(23.726598, 37.971515),
			point : {
				pixelSize : 5,
				color : Color.RED,
				outlineColor : Color.WHITE,
				outlineWidth : 2
			},
			label : {
				text : 'Zoakinoula',
				font : '14pt monospace',
				style: LabelStyle.FILL_AND_OUTLINE,
				outlineWidth : 2,
				verticalOrigin : VerticalOrigin.BOTTOM,
				pixelOffset : new Cartesian2(0, -9)
			}
		});
	}

	var viewer;

	init_cesium();
	init_ui();

	viewer.zoomTo(viewer.entities);

});
