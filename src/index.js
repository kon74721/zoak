require('cesium/Source/Widgets/widgets.css');
var BuildModuleUrl = require('cesium/Source/Core/buildModuleUrl');
BuildModuleUrl.setBaseUrl('./');

var Viewer = require('cesium/Source/Widgets/Viewer/Viewer');
var Cartesian2 = require('cesium/Source/Core/Cartesian2');
var Cartesian3 = require('cesium/Source/Core/Cartesian3');
var Color = require('cesium/Source/Core/Color');
var VerticalOrigin = require('cesium/Source/Scene/VerticalOrigin');
var LabelStyle = require('cesium/Source/Scene/LabelStyle');
//var Cesium = require('cesium/Source/Cesium');

var viewer = new Viewer('cesiumContainer');

var citizensBankPark = viewer.entities.add({
  name : 'Zoakinoula',
  //position : Cartesian3.fromDegrees(37.971515, 23.726598),
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

viewer.zoomTo(viewer.entities);
