'''

Connector mod

Components:
 Joint auto-connector
 Auto-pad'der

 Usage:
 	import OG_MayaTools.connector_mod as conmod
	reload(conmod)
	conmod.gui()
'''

import pymel.core as pm
import maya.cmds as cmds
import sys

windowWidth = 500
windowHeight=300
buttonWidth = 150
keepAliveCheck = ""
windowKeepAlive=True
__green__ = 14
__red__ = 13
__blue__ = 6

def toast(message):
    cmds.headsUpMessage(message)

def getSelected(niceName=False, dagOption=True):
	selectedItem = cmds.ls(sl=True, dag=dagOption)
	if niceName == True:
		return selectedItem[0]
	else:
		return selectedItem

def closeWindow():
	global connector_window, windowKeepAlive
	if windowKeepAlive==True:
		pm.deleteUI(connector_window)

def selectItem(*args):
	# Break down the passed selected into
	#selItem = getSelected(False, True)
	pm.text("padObject", label=str(getSelected(True)), edit=True)

def padObject(*args):
	global appendPad
	# Get the location of the object getting padded (xform)
	initialObject  = getSelected()
	initialTranslate = cmds.xform(initialObject[0], q=True, t=True)
	initialRotate = cmds.xform(initialObject[0], q=True, ro=True)
	# Create group
	padName = str(getSelected(True))
	if appendPad.getValue() == True:
		padName = padName + "_pad"
	pm.group(em=True, n=padName)
	# Move group to location of object
	cmds.xform(padName, t=initialTranslate, ro=initialRotate)
	# Move object into group
	cmds.parent(initialObject[0], padName)
	#toast(windowKeepAlive.getValue)
	#if windowKeepAlive.getValue
	closeWindow()

def create_circle(shapeTitle):
    return pm.circle(
        c=(0, 0, 0),
        ch=1,
        d=3,
        ut=0,
        sw=360,
        s=8,
        r=1,
        tol=0.01,
        nr=(0, 1, 0),
        name=shapeTitle,
        )


def create_square(shapeTitle):
    return pm.curve(name=shapeTitle, p=[(0.5, 0, 0.5), (-0.5, 0, 0.5),
                    (-0.5, 0, -0.5), (0.5, 0, -0.5), (0.5, 0, 0.5)],
                    k=[0, 1, 2, 3, 4], d=1)


def create_2darrow(shapeTitle):
    return pm.curve(name=shapeTitle, p=[(0, 0, 1), (1, 0, 0), (0.5, 0, 0), (0.5, 0, -1), (-0.5, 0, -1), (-0.5, 0, 0), (-1, 0, 0), (0, 0, 1)], k=[0, 1, 2, 3, 4, 5, 6, 7], d=1)


def create_3darrow(shapeTitle):
    return pm.curve(name=shapeTitle, p=[(0, 0, 1), (1, 0, 0), (0.5, 0, 0),
    	(0.5, 0, -1), (0, 0, -1), (0, 0.5, -1), (0, 0.5, 0), (0, 1, 0),
    	(0, 0, 1), (-1, 0, 0), (-0.5, 0, 0), (-0.5, 0, -1), (0, 0, -1),
    	(0, -0.5, -1), (0, -0.5, 0), (0, -1, 0), (0, 0, 1)],
    	k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], d=1)


def create_cube(shapeTitle):
    return pm.curve(name=shapeTitle, p=[(0.5, 0.5, -0.5), (0.5, 0.5, 0.5),
        (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5,
            -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5),
        (-0.5, -0.5, 0.5), (-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, 0.5,
            0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5)],
        k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], d=1)


def create_COG(shapeTitle):
        return pm.curve(name=shapeTitle, p=[(-1.19209e-07, 0, 2), (-0.382683, 0, 0.923879), (-1.414213, 0, 1.414213), (-0.923879, 0, 0.382683), (-2, 0, 0), (-0.923879, 0, -0.382683), (-1.414213, 0, -1.414214), (-0.382683, 0, -0.923879), (0, 0, -2), (0.382683, 0, -0.923879), (1.414214, 0, -1.414213), (0.92388, 0, -0.382683), (2, 0, -1.19209e-07), (0.92388, 0, 0.382683), (1.414214, 0, 1.414213), (0.382683, 0, 0.923879), (-1.19209e-07, 0, 2)], k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 14], d=3)

def create_sphere(shapeTitle):
        return pm.curve(name=shapeTitle, p=[(0, 1, 0), (0.25, 0.866025, 0.433013), (0.5, 0.866025, 0), (0.25, 0.866025, -0.433013), (-0.25, 0.866025, -0.433013), (-0.5, 0.866025, -7.45058e-08), (-0.25, 0.866025, 0.433013), (0.25, 0.866025, 0.433013), (0.433013, 0.5, 0.75), (-0.433013, 0.5, 0.75), (-0.866025, 0.5, -1.29048e-07), (-0.433013, 0.5, -0.75), (0.433013, 0.5, -0.75), (0.866025, 0.5, 0), (0.433013, 0.5, 0.75), (0.5, 0, 0.866025), (-0.5, 0, 0.866025), (-1, 0, -1.49012e-07), (-0.5, 0, -0.866026), (0.5, 0, -0.866025), (1, 0, 0), (0.5, 0, 0.866025), (0.433013, -0.5, 0.75), (-0.433013, -0.5, 0.75), (-0.866025, -0.5, -1.29048e-07), (-0.433013, -0.5, -0.75), (0.433013, -0.5, -0.75), (0.866025, -0.5, 0), (0.433013, -0.5, 0.75), (0.25, -0.866025, 0.433013), (-0.25, -0.866025, 0.433013), (-0.5, -0.866025, -7.45058e-08), (-0.25, -0.866025, -0.433013), (0.25, -0.866025, -0.433013), (0.5, -0.866025, 0), (0.25, -0.866025, 0.433013), (0, -1, 0), (-0.25, -0.866025, -0.433013), (-0.433013, -0.5, -0.75), (-0.5, 0, -0.866026), (-0.433013, 0.5, -0.75), (-0.25, 0.866025, -0.433013), (0, 1, 0), (-0.5, 0.866025, -7.45058e-08), (-0.866025, 0.5, -1.29048e-07), (-1, 0, -1.49012e-07), (-0.866025, -0.5, -1.29048e-07), (-0.5, -0.866025, -7.45058e-08), (0, -1, 0), (0.5, -0.866025, 0), (0.866025, -0.5, 0), (1, 0, 0), (0.866025, 0.5, 0), (0.5, 0.866025, 0), (0, 1, 0), (0.25, 0.866025, -0.433013), (0.433013, 0.5, -0.75), (0.5, 0, -0.866025), (0.433013, -0.5, -0.75), (0.25, -0.866025, -0.433013), (0, -1, 0), (-0.25, -0.866025, 0.433013), (-0.433013, -0.5, 0.75), (-0.5, 0, 0.866025), (-0.433013, 0.5, 0.75), (-0.25, 0.866025, 0.433013), (0, 1, 0)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], d=1)

def create_roundpointer(shapeTitle):
        return pm.curve(name=shapeTitle, p=[(7.78772e-08, 1.94693e-08, 1), (0, 1, 0), (0.707107, 0.707107, 0), (1, 0, 0), (0.707107, -0.707107, 0), (0, -1, 0), (-0.707107, -0.707107, 0), (-1, 0, 0), (-0.707107, 0.707107, 0), (0, 1, 0), (0, 0.923879, -0.382683), (0.653281, 0.653281, -0.382683), (0.92388, 0, -0.382683), (0.653281, -0.653281, -0.382683), (0, -0.923879, -0.382683), (-0.653281, -0.653281, -0.382683), (-0.923879, 0, -0.382683), (-0.653281, 0.653281, -0.382683), (0, 0.923879, -0.382683), (0, 0.707107, -0.707107), (0.5, 0.5, -0.707107), (0.707107, 0, -0.707107), (0.5, -0.5, -0.707107), (0, -0.707107, -0.707107), (-0.5, -0.5, -0.707107), (-0.707107, 0, -0.707107), (-0.5, 0.5, -0.707107), (0, 0.707107, -0.707107), (0, 0.382683, -0.92388), (0.270598, 0.270598, -0.92388), (0.382683, 0, -0.92388), (0.270598, -0.270598, -0.92388), (0, -0.382683, -0.92388), (-0.270598, -0.270598, -0.92388), (-0.382683, 0, -0.92388), (-0.270598, 0.270598, -0.92388), (0, 0.382683, -0.92388), (0, 0, -1), (0, -0.382683, -0.92388), (0, -0.707107, -0.707107), (0, -0.923879, -0.382683), (0, -1, 0), (7.78772e-08, 1.94693e-08, 1), (0.707107, -0.707107, 0), (0.653281, -0.653281, -0.382683), (0.5, -0.5, -0.707107), (0.270598, -0.270598, -0.92388), (0, 0, -1), (-0.270598, 0.270598, -0.92388), (-0.5, 0.5, -0.707107), (-0.653281, 0.653281, -0.382683), (-0.707107, 0.707107, 0), (7.78772e-08, 1.94693e-08, 1), (0.707107, 0.707107, 0), (0.653281, 0.653281, -0.382683), (0.5, 0.5, -0.707107), (0.270598, 0.270598, -0.92388), (0, 0, -1), (-0.270598, -0.270598, -0.92388), (-0.5, -0.5, -0.707107), (-0.653281, -0.653281, -0.382683), (-0.707107, -0.707107, 0), (7.78772e-08, 1.94693e-08, 1)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], d=1)

def create_compass(shapeTitle): 
    newShape = pm.curve(name="Microedge1", p=[(-0.309017, 0, -0.951057),
        (-0.455125, 0, -0.882908), (-0.587785, 0, -0.809017), (-0.710365, 0,
            -0.710365), (-0.809017, 0, -0.587785), (-0.885102, 0, -0.457095),
        (-0.951057, 0, -0.309017)], k=[0, 0, 0, 1, 2, 3, 4, 4, 4], d=3)
    sidepiece1 = newShape
    sidepiece_shape1 = sidepiece1.getShape();
    sidepiece_shape1.overrideEnabled.set(True)
    newShape = pm.curve(name="Microedge2", p=[(0.309017, 0, -0.951057),
        (0.457095, 0, -0.885102), (0.587785, 0, -0.809017), (0.709632, 0,
            -0.70902), (0.809017, 0, -0.587785), (0.885102, 0, -0.457095),
        (0.951057, 0, -0.309017)], k=[0, 0, 0, 1, 2, 3, 4, 4, 4], d=3)
    sidepiece2 = newShape
    sidepiece_shape2 = newShape.getShape();
    sidepiece_shape2.overrideEnabled.set(True)
    newShape = pm.curve(name="Microedge3", p=[(0.951057, 0, 0.309017),
        (0.885102, 0, 0.457095), (0.809017, 0, 0.587785), (0.710365, 0,
            0.710365), (0.587785, 0, 0.809017), (0.455125, 0, 0.882908),
        (0.309017, 0, 0.951057)], k=[0, 0, 0, 1, 2, 3, 4, 4, 4], d=3)
    sidepiece3 = newShape
    sidepiece_shape3 = newShape.getShape();
    sidepiece_shape3.overrideEnabled.set(True)
    newShape = pm.curve(name="Microedge4", p=[(-0.309017, 0, 0.951057),
        (-0.457095, 0, 0.885102), (-0.587785, 0, 0.809017), (-0.710365, 0,
            0.710365), (-0.809017, 0, 0.587785), (-0.882908, 0, 0.455125),
        (-0.951057, 0, 0.309017)], k=[0, 0, 0, 1, 2, 3, 4, 4, 4], d=3)
    sidepiece4 = newShape
    sidepiece_shape4 = newShape.getShape();
    sidepiece_shape4.overrideEnabled.set(True)
    microedge = pm.parent(shape="relative")
    backCompass = pm.curve(name="compassBack", p=[(0.309017, 0, 0.951057),
        (0.309017, 0, 1.296348), (0.548167, 0, 1.296348), (0, 0, 2),
        (-0.548167, 0, 1.296347), (-0.309017, 0, 1.296347), (-0.309017, 0,
            0.951057)], k=[0, 1, 2, 3, 4, 5, 6], d=1)
    leftCompass = pm.curve(name="compassLeft", p=[(0.309017, 0, 0.951057),
        (0.309017, 0, 1.296348), (0.548167, 0, 1.296348), (0, 0, 2),
        (-0.548167, 0, 1.296347), (-0.309017, 0, 1.296347), (-0.309017, 0,
            0.951057)], k=[0, 1, 2, 3, 4, 5, 6], d=1)
    forwardCompass = pm.curve(name="compassForward", p=[(0.309017, 0,
        0.951057), (0.309017, 0, 1.296348), (0.548167, 0, 1.296348), (0, 0,
        2), (-0.548167, 0, 1.296347), (-0.309017, 0, 1.296347), (-0.309017,
        0, 0.951057)], k=[0, 1, 2, 3, 4, 5, 6], d=1)
    rightCompass = pm.curve(name="compassRight", p=[(0.309017, 0, 0.951057),
        (0.309017, 0, 1.296348), (0.548167, 0, 1.296348), (0, 0, 2),
        (-0.548167, 0, 1.296347), (-0.309017, 0, 1.296347), (-0.309017, 0,
            0.951057)], k=[0, 1, 2, 3, 4, 5, 6], d=1)
    leftCompass.ry.set(90)
    backCompass.ry.set(180)
    rightCompass.ry.set(270)
    forwardCompass_shape = forwardCompass.getShape()
    backCompass_shape = backCompass.getShape()
    leftCompass_shape = leftCompass.getShape()
    rightCompass_shape = rightCompass.getShape()
    forwardCompass_shape.overrideEnabled.set(True)
    backCompass_shape.overrideEnabled.set(True)
    leftCompass_shape.overrideEnabled.set(True)
    rightCompass_shape.overrideEnabled.set(True)
    forwardCompass_shape.overrideColor.set(__green__)
    backCompass_shape.overrideColor.set(__green__)
    leftCompass_shape.overrideColor.set(__blue__)
    rightCompass_shape.overrideColor.set(__red__)
    pm.makeIdentity(sidepiece1, sidepiece2, sidepiece3, sidepiece4, n=0, s=1,
        r=1, t=1, apply=True, pn=1)
    pm.makeIdentity(leftCompass, rightCompass, forwardCompass, backCompass,
        n=0, s=1, r=1, t=1, apply=True, pn=1)
    newGroup = pm.group(name="microEdges", em=True)
    pm.parent(sidepiece_shape1, sidepiece_shape2, sidepiece_shape3,
        sidepiece_shape4, forwardCompass_shape, backCompass_shape, leftCompass_shape,
        rightCompass_shape, newGroup, s=True, r=True)
    pm.makeIdentity(newGroup, n=0, s=1, r=1, t=1, apply=True, pn=1)
    pm.delete(sidepiece1, sidepiece2, sidepiece3, sidepiece4)
    pm.delete(forwardCompass, backCompass, leftCompass, rightCompass)
    shapeName = pm.rename(newGroup, shapeTitle)
    return newGroup

def fkikSelectRoot(*args):
	rootJoint.setText(getSelected(True))

def createShape(*args):
	print(args[0].getValue())
	print(args[1].getText())
	print(args[2].getText())
	print(args[3].getValue())
	shapeObject = args[0].getValue()
	shapeName = args[1].getText()
	shapeSuffix = args[2].getText()
	shapeLocation = args[3].getValue()
	if shapeName == "":
		shapeName = "shape"
	if shapeSuffix == "":
		shapeSuffix = "_icon"
	shapeName = shapeName + shapeSuffix
	#determine which pulldown item is chosen
	#if build to appropriate functino
	if shapeObject == "Circle":
		newShape = create_circle(shapeName)
	elif shapeObject == "Sphere":
		newShape = create_sphere(shapeName)
	elif shapeObject == "Square":
		newShape = create_square(shapeName)
	elif shapeObject == "2D Arrow":
		newShape = create_2darrow(shapeName)
	elif shapeObject == "3D Arrow":
		newShape = create_3darrow(shapeName)
	elif shapeObject == "Round Pointer":
		newShape = create_roundpointer(shapeName)
	elif shapeObject == "Compass":
		newShape = create_compass(shapeName)
	elif shapeObject == "COG Circle":
		newShape = create_COG(shapeName)
	elif shapeObject == "Cube":
		newShape = create_cube(shapeName)
	else:
		print("Shape unidentified - " + str(shapeName))
		return


	#rename curve
	#move curve to desired locaiton, if not set to origin

def autocloseWindowToggle(*args):
	windowKeepAlive = keepAliveCheck.getValue()


def gui():
	global connector_window, appendPad, rootJoint, windowKeepAlive, keepAliveCheck
	connector_window = pm.window(title="Connector Window", width=windowWidth, height=windowHeight, sizeable=True)
	pm.columnLayout(numberOfChildren=2, columnAlign="left")
	mainTabs = pm.tabLayout(innerMarginWidth=5, innerMarginHeight=5)

	tab_1 = pm.columnLayout(numberOfChildren=2)
	# Tab1 begin
	pm.text(label="<i>Things to work on</i>")
	pm.text(label="Autosnapper\nJoint connector\nShape maker integration", align="left")
	pm.setParent(mainTabs)
	# Tab1 end


	tab_2 = pm.scrollLayout(width=windowWidth-10, height=windowHeight-50)
	#Tab 2 begin
	pm.frameLayout(collapsable=True, label="Pad Object", width=(windowWidth-10))

	pm.rowLayout(numberOfColumns=3, columnWidth=[(1, 150), (2, 200), (3, 150)], columnAlign=[(3, 'right')])
	pm.text(label="Choose an object to pad:")
	pm.text("padObject", label="<i>nothing selected</i>")
	pm.button(label="Choose item", command=pm.Callback(selectItem))
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=2, columnWidth=[(1,350)])
	pm.text("Automatically append \"_pad\" to end?")
	appendPad = pm.checkBox("appendPad", value=True, label="")
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=3)
	pm.text(width=150, label="")
	pm.button(label="Pad this", command=pm.Callback(padObject))
	pm.text(width=150, label="")
	pm.setParent("..")

	pm.setParent(mainTabs)
	#Tab 2 end

	tab_3 = pm.columnLayout(numberOfChildren=2, columnAlign="left")
	pm.frameLayout(label="Choose options:", width=450)
	
	pm.rowLayout(numberOfColumns=2, columnAlign=([1, "left"], [2, "right"]), width=450, columnWidth=([1, 200], [2, 250]))
	pm.text(label="Choose a shape:")
	shapeOptions = pm.optionMenu(width=100)
	pm.menuItem(label="Circle")
	pm.menuItem(label="Sphere")
	pm.menuItem(label="Square")
	pm.menuItem(label="Cube")
	pm.menuItem(label="2D Arrow")
	pm.menuItem(label="3D Arrow")
	pm.menuItem(label="Round Pointer")
	pm.menuItem(label="COG Circle")
	pm.menuItem(label="Compass")
	pm.setParent("..")
	
	pm.rowLayout(numberOfColumns=2, columnAlign=([1, "left"], [2, "right"]), width=450, columnWidth=([1, 200], [2, 250]))
	pm.text(label="Enter a name.\nLeave blank for default shape name.")
	shapeName = pm.textField(placeholderText="shape")
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=2, columnAlign=([1, "left"], [2, "right"]), width=450, columnWidth=([1, 200], [2, 250]))
	pm.text(label="Insert a suffix.\nLeave blank for default\n\"_icon\" to be added")
	shapeSuffix = pm.textField(placeholderText="_icon")
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=2, columnAlign=([1, "left"], [2, "right"]), width=450, columnWidth=([1, 200], [2, 250]))
	pm.text(label="Shape is placed on:")
	placementOption = pm.optionMenu(width=150)
	pm.menuItem(label="Origin")
	pm.menuItem(label="Currently Selected Object")
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=1, columnAlign=([1, "center"]), width=450, columnWidth=([1,450]))
	pm.button(label="Create Shape", command=pm.Callback(createShape, shapeOptions, shapeName, shapeSuffix, placementOption))
	pm.setParent("..")

	pm.setParent(mainTabs)
	#Tab 3 end

	tab_4 = pm.columnLayout(numberOfChildren=1, columnAlign="left")
	pm.rowLayout(numberOfColumns=3, width=450, columnWidth=([1, 150], [2, 200], [3, 150]))
	pm.text(label="Select the root joint:")
	rootJoint = pm.textField(placeholderText="none set", editable=False)
	pm.button(label="Select root", command=pm.Callback(fkikSelectRoot))
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=2, width=450, columnWidth=([1, 350], [2, 150]))
	pm.text(label="Create controls on respective joints?")
	pm.checkBox("", value=True)
	pm.setParent("..")

	pm.setParent(mainTabs)

	pm.setParent("..")

	mainTabs.setTabLabel([tab_1, "TODO"])
	mainTabs.setTabLabel([tab_2, "Snapper"])
	mainTabs.setTabLabel([tab_3, "Shape Maker"])
	mainTabs.setTabLabel([tab_4, "FK/IK Creator"])

	

	keepAliveCheck = pm.checkBox("Automatically close window", value=windowKeepAlive, changeCommand=pm.Callback(autocloseWindowToggle))

	pm.showWindow(connector_window)