import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
if mc.window("switchAttr", exists=True):
    mc.deleteUI("switchAttr")
mc.window("switchAttr", t="Attribute reorder", w=400, h=50,menuBar=1)
mc.columnLayout(w=400)
mc.button(l="refresh list",c="refreshList()",w=400)
mc.button(l="reorder attributes",c="reorderAttr()",w=400)
mc.setParent("..")
mc.setParent("..")
layout = cmds.formLayout()

treeList = mc.treeView( parent = layout, abr = False ,arp = 0)

mc.formLayout(layout,e=True, attachForm=(treeList,'top', 2))
mc.formLayout(layout,e=True, attachForm=(treeList,'left', 2))
mc.formLayout(layout,e=True, attachForm=(treeList,'bottom', 2))
mc.formLayout(layout,e=True, attachForm=(treeList,'right', 2))
mc.setParent("..")
mc.setParent("..")


mc.setParent("..")
mc.showWindow()
Node =[]
Number = []
def refreshList():
    mc.treeView(treeList,e=1,ra=1)
    
    
    try:
        mc.select(Attr.entry[0].selOrg ,r=1)
        Attr.entry.clear()
    except:
        pass
    
    selOrg = mc.ls(sl=1)
    if selOrg == []:
        mc.error("you need to select an object first to list the attributes")
        return
    attr = pm.listAttr(k=1)
    try:
        attr.remove('visibility')
    except ValueError:
        pass
    try:
        attr.remove('translateX')
    except ValueError:
        pass
    try:
        attr.remove('translateY')
    except ValueError:
        pass
    try:
        attr.remove('translateZ')
    except ValueError:
        pass
    try:
        attr.remove('rotateX')
    except ValueError:
        pass
    try:
        attr.remove('rotateY')
    except ValueError:
        pass
    try:
        attr.remove('rotateZ')
    except ValueError:
        pass
    try:
        attr.remove('scaleX')
    except ValueError:
        pass
    try:
        attr.remove('scaleY')
    except ValueError:
        pass
    try:
        attr.remove('scaleZ')
    except ValueError:
        pass
    
    length =len(attr)
    #print(attr)
    for _ in range(length):
        Node.append(attr[_])
        Number.append(_)
        strNum = str(_)
        
        create()
        
        
        Node.clear()
        Number.clear()
   
listNewOrder = []
def reorderAttr():
    listNewOrder.clear()
    length =len(Attr.entry)
    #list = mc.treeView( treeList, q=1, it=1)
    #print(list)
    for _ in range(length):
        #print(Attr.entry[_].name)
        newOrder = mc.treeView( treeList, q=1, idx=Attr.entry[_].name)
        #print(newOrder)
        #print(Attr.entry[_].name+" "+str(newOrder))
        listNewOrder.insert(newOrder,Attr.entry[_].number)
        mc.select(Attr.entry[_].selOrg,r=1)
        mc.deleteAttr(at =Attr.entry[_].name )
    
    newLength =len(listNewOrder)
    
    for _ in range(newLength):
        
        num = listNewOrder[_]
        strSelOrg = str(Attr.entry[num].selOrg)
        if Attr.entry[num].type == "double":
            if Attr.entry[num].MinExis == 0:
                if Attr.entry[num].MaxExis == 0:
                    attr = mc.addAttr(at="double",k=1,ln=Attr.entry[num].name,dv = Attr.entry[num].defVal[0])
                    strAttr = str(Attr.entry[num].name)
                    if None == Attr.entry[num].OutConnection:
                        if None == Attr.entry[num].InConnection:
                            #notWork
                            print("")
                        else:
                            for node in Attr.entry[num].InConnection:
                                mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                    if None == Attr.entry[num].InConnection:
                        if None == Attr.entry[num].OutConnection:
                            #notWork
                            print("")
                        else:
                            for node in Attr.entry[num].OutConnection:
                                mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
                    if None != Attr.entry[num].InConnection and None != Attr.entry[num].OutConnection :
                        
        
                        strSelOrg = str(Attr.entry[num].selOrg)
                        for node in Attr.entry[num].InConnection:
                            mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                        for node in Attr.entry[num].OutConnection:
                            mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
                else:
                    attr=mc.addAttr(at="double",k=1,ln=Attr.entry[num].name,max=Attr.entry[num].Max[0],dv = Attr.entry[num].defVal[0])
                    strAttr = str(Attr.entry[num].name)
                    if None == Attr.entry[num].OutConnection:
                        if None == Attr.entry[num].InConnection:
                            #notWork
                            print("")
                        else:
                            for node in Attr.entry[num].InConnection:
                                mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                    if None == Attr.entry[num].InConnection:
                        if None == Attr.entry[num].OutConnection:
                            #notWork
                            print("")
                        else:
                            for node in Attr.entry[num].OutConnection:
                                mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
                    if None != Attr.entry[num].InConnection and None != Attr.entry[num].OutConnection :
                        
        
                        strSelOrg = str(Attr.entry[num].selOrg)
                        for node in Attr.entry[num].InConnection:
                            mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                        for node in Attr.entry[num].OutConnection:
                            mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
            if Attr.entry[num].MinExis == 1:
               
                if Attr.entry[num].MaxExis == 0:
                    attr = mc.addAttr(at="double",k=1,ln=Attr.entry[num].name,min=Attr.entry[num].Min[0],dv = Attr.entry[num].defVal[0])
                    strAttr = str(Attr.entry[num].name)
                    if None == Attr.entry[num].OutConnection:
                        if None == Attr.entry[num].InConnection:
                            #notWork
                            print("")
                        else:
                            for node in Attr.entry[num].InConnection:
                                mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                    if None == Attr.entry[num].InConnection:
                        if None == Attr.entry[num].OutConnection:
                            #notWork
                            print("")
                        else:
                            for node in Attr.entry[num].OutConnection:
                                mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
                    if None != Attr.entry[num].InConnection and None != Attr.entry[num].OutConnection :
                        
        
                        strSelOrg = str(Attr.entry[num].selOrg)
                        for node in Attr.entry[num].InConnection:
                            mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                        for node in Attr.entry[num].OutConnection:
                            mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
                else:
                    attr =mc.addAttr(at="double",k=1,ln=Attr.entry[num].name,max=Attr.entry[num].Max[0],min=Attr.entry[num].Min[0],dv = Attr.entry[num].defVal[0])
                    strAttr = str(Attr.entry[num].name)
                    if None == Attr.entry[num].OutConnection:
                        if None == Attr.entry[num].InConnection:
                            #notWork
                            print("")
                        else:
                            for node in Attr.entry[num].InConnection:
                                mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                    if None == Attr.entry[num].InConnection:
                        if None == Attr.entry[num].OutConnection:
                            #notWork
                            print("")
                        else:
                            for node in Attr.entry[num].OutConnection:
                                mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
                    if None != Attr.entry[num].InConnection and None != Attr.entry[num].OutConnection :
                        
        
                        strSelOrg = str(Attr.entry[num].selOrg)
                        for node in Attr.entry[num].InConnection:
                            mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                        for node in Attr.entry[num].OutConnection:
                            mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
        if Attr.entry[num].type == "long":
        
            if Attr.entry[num].MinExis == 0:
               
                if Attr.entry[num].MaxExis == 0:
                    attr = mc.addAttr(at="long",k=1,ln=Attr.entry[num].name,dv = Attr.entry[num].defVal[0])
                    strAttr = str(Attr.entry[num].name)
                    if None == Attr.entry[num].OutConnection:
                        if None == Attr.entry[num].InConnection:
                            #notWork
                            print("")
                        else:
                            for node in Attr.entry[num].InConnection:
                                mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                    if None == Attr.entry[num].InConnection:
                        if None == Attr.entry[num].OutConnection:
                            #notWork
                            print("")
                        else:
                            for node in Attr.entry[num].OutConnection:
                                mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
                    if None != Attr.entry[num].InConnection and None != Attr.entry[num].OutConnection :
                        
        
                        strSelOrg = str(Attr.entry[num].selOrg)
                        for node in Attr.entry[num].InConnection:
                            mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                        for node in Attr.entry[num].OutConnection:
                            mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
                else:
                    attr=mc.addAttr(at="long",k=1,ln=Attr.entry[num].name,max=Attr.entry[num].Max[0],dv = Attr.entry[num].defVal[0])
                    strAttr = str(Attr.entry[num].name)
                    if None == Attr.entry[num].OutConnection:
                        if None == Attr.entry[num].InConnection:
                            #notWork
                            print("")
                        else:
                            for node in Attr.entry[num].InConnection:
                                mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                    if None == Attr.entry[num].InConnection:
                        if None == Attr.entry[num].OutConnection:
                            #notWork
                            print("")
                        else:
                            for node in Attr.entry[num].OutConnection:
                                mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
                    if None != Attr.entry[num].InConnection and None != Attr.entry[num].OutConnection :
                        
        
                        strSelOrg = str(Attr.entry[num].selOrg)
                        for node in Attr.entry[num].InConnection:
                            mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                        for node in Attr.entry[num].OutConnection:
                            mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
            if Attr.entry[num].MinExis == 1:
            
                if Attr.entry[num].MaxExis == 0:
                    attr = mc.addAttr(at="long",k=1,ln=Attr.entry[num].name,min=Attr.entry[num].Min[0],dv = Attr.entry[num].defVal[0])
                    strAttr = str(Attr.entry[num].name)
                    if None == Attr.entry[num].OutConnection:
                        if None == Attr.entry[num].InConnection:
                            #notWork
                            print("")
                        else:
                            for node in Attr.entry[num].InConnection:
                                mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                    if None == Attr.entry[num].InConnection:
                        if None == Attr.entry[num].OutConnection:
                            #notWork
                            print("")
                        else:
                            for node in Attr.entry[num].OutConnection:
                                mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
                    if None != Attr.entry[num].InConnection and None != Attr.entry[num].OutConnection :
                        
        
                        strSelOrg = str(Attr.entry[num].selOrg)
                        for node in Attr.entry[num].InConnection:
                            mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                        for node in Attr.entry[num].OutConnection:
                            mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
                else:
                    attr = mc.addAttr(at="long",k=1,ln=Attr.entry[num].name,max=Attr.entry[num].Max[0],min=Attr.entry[num].Min[0],dv = Attr.entry[num].defVal[0])
                    strAttr = str(Attr.entry[num].name)
                    if None == Attr.entry[num].OutConnection:
                        if None == Attr.entry[num].InConnection:
                            #notWork
                            print("")
                        else:
                            for node in Attr.entry[num].InConnection:
                                mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                    if None == Attr.entry[num].InConnection:
                        if None == Attr.entry[num].OutConnection:
                            #notWork
                            print("")
                        else:
                            for node in Attr.entry[num].OutConnection:
                                mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
                    if None != Attr.entry[num].InConnection and None != Attr.entry[num].OutConnection :
                        
        
                        strSelOrg = str(Attr.entry[num].selOrg)
                        for node in Attr.entry[num].InConnection:
                            mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                        for node in Attr.entry[num].OutConnection:
                            mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
        if Attr.entry[num].type == "bool":
            attr = mc.addAttr(at="bool",k=1,ln=Attr.entry[num].name)
            strAttr = str(Attr.entry[num].name)
            if None == Attr.entry[num].OutConnection:
                if None == Attr.entry[num].InConnection:
                    #notWork
                    print("")
                else:
                    for node in Attr.entry[num].InConnection:
                        mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
            if None == Attr.entry[num].InConnection:
                if None == Attr.entry[num].OutConnection:
                    #notWork
                    print("")
                else:
                    for node in Attr.entry[num].OutConnection:
                        mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
            if None != Attr.entry[num].InConnection and None != Attr.entry[num].OutConnection :

                strSelOrg = str(Attr.entry[num].selOrg)
                for node in Attr.entry[num].InConnection:
                    mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                for node in Attr.entry[num].OutConnection:
                    mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
        if Attr.entry[num].type == "enum":
            length = len(Attr.entry[num].EnumList)
            en = []
            for _ in range(length):
                string = str(Attr.entry[num].EnumList[_]+":")
                en.append(string)
            enum = ''.join(en)
            attr = mc.addAttr(at="enum",k=1,ln=Attr.entry[num].name,en=enum)
            strAttr = str(Attr.entry[num].name)
            if None == Attr.entry[num].OutConnection:
                if None == Attr.entry[num].InConnection:
                    #notWork
                    print("")
                else:
                    for node in Attr.entry[num].InConnection:
                        mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
            if None == Attr.entry[num].InConnection:
                if None == Attr.entry[num].OutConnection:
                    #notWork
                    print("")
                else:
                    for node in Attr.entry[num].OutConnection:
                        mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
            if None != Attr.entry[num].InConnection and None != Attr.entry[num].OutConnection :
                

                print(Attr.entry[num].InConnection)
                strSelOrg = str(Attr.entry[num].selOrg)
                for node in Attr.entry[num].InConnection:
                    mc.connectAttr(node,strSelOrg+"."+strAttr,f=1)
                for node in Attr.entry[num].OutConnection:
                    mc.connectAttr(strSelOrg+"."+strAttr,node,f=1)
                
                                          
    print(listNewOrder)
    mc.treeView(treeList,e=1,ra=1)
    
    mc.select(Attr.entry[0].selOrg ,r=1)
    Attr.entry.clear()
    refreshList()
    
        
def create():
    p1 = Attr('one',"d")

class Attr(object):
    entry = []

    def __init__(self, node, number):
        
        Attr.entry.append(self)
        selOrg = mc.ls(sl=1)
        self.selOrg = selOrg[0]
        self.num = str(len(Attr.entry))
        self.node = mc.treeView( treeList, e=True, addItem = (Node[0], ""))
        self.name = Node[0]
        self.number = Number[0]
        #determine all connections
        self.OutConnection = mc.listConnections(selOrg[0]+"."+Node[0],p=1,s=0)
        self.InConnection = mc.listConnections(selOrg[0]+"."+Node[0],p=1,d=0)
        #determine all component of the attribute.
        self.type = mc.attributeQuery(Node,node=selOrg[0],at=1)
        self.defVal = mc.attributeQuery(Node,node=selOrg[0],ld=1)
        self.MinExis = mc.attributeQuery(Node,node=selOrg[0],mne=1)
        self.Min = []
        if self.MinExis == 1:
            Mini = mc.attributeQuery(Node,node=selOrg[0],min=1)
            self.Min.append(Mini[0])
       
        self.MaxExis = mc.attributeQuery(Node,node=selOrg[0],mxe=1)
        self.Max = []
        if self.MaxExis == 1:
            Maxi = mc.attributeQuery(Node,node=selOrg[0],max=1)
            self.Max.append(Maxi[0])
        self.Enum = mc.attributeQuery(Node,node=selOrg[0],e=1)
        self.EnumList = mc.attributeQuery(Node,node=selOrg[0],le=1)

    def getPar(self):
            selOrg = mc.ls(sl=1)
            self.name.setText(selOrg[0])