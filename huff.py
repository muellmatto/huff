#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node(object):
        # Wenn wir eine Instanz dieser Klasse
        # erstellen, müssen wir zwingend einen
        # Schlüssel und einen Zähler übergeben,
        # diese können auch None bzw 0 sein
    def __init__(self, key, count):
        """Konstruktor, initialisiert den
        Schlüssel und die Häufigkeit"""

        # Ein neuer Knoten hat zunächst keinen
        # Elternknoten und keine Kinderknoten.
        self.count = count
        self.key = key
        self.parent = None
        self.leftChild = None
        self.rightChild = None
    
    # Die folgenden zwei Methoden erlauben es
    # einem Knoten einen Kinderknoten zuzuordnen.
    # Zuerst setzt der Knoten sich selbst als
    # Elternknoten des neuen Kindes,
    # danach setzt der Knoten den neuen Knoten
    # als eigenes Kind fest.
    # Hierdurch sind die Knoten in beide
    # Richtungen verknüpft.
    # In dieser Implementation ist die Wurzel
    # dadurch gekennzeichnet, dass
    # self.parent==None ist, also kein
    # Elternknoten gesetzt ist.
    def setLeftChild(self, node):
        """ Setzt das linke Kind und aktualisiert
        den Elternknoten """
        node.parent = self
        self.leftChild = node
    def setRightChild(self, node):
        """ Setzt das rechte Kind und aktualisiert
        den Elternknoten """
        node.parent = self
        self.rightChild = node
        

    # Der Knoten muss herausfinden können,
    # ob er linkes oder rechtes Kind ist,
    # da über diese Unterscheidung später
    # das Codewort generiert wird.
    # Wir lösen dies über boolsche
    # Funktionen.
    def isLeftChild(self):
        """ Prüft, ob der Knoten am Elternknoten
        das linke Kind ist"""
        return (self.parent is not None) and (self.parent.leftChild == self)
    
    def isRightChild(self):
        """ Prüft, ob der Knoten am Elternknoten
        das rechte Kind ist"""
        return (self.parent is not None) and (self.parent.rightChild == self)
    
    # Die Methode getCode nutzt die beiden
    # zuvor definierten Methoden, um das Codewort
    # eines Knoten zu konstruieren.
    def getCode(self):
        """ Folgt dem Pfad eines Knotens zur Wurzel
        und erzeugt ein Codewort"""
        # Wir benutzen die Variable currentNode als
        # Platzhalter für den gerade betrachteten Knoten
        # und starten im Blatt selbst.
        currentNode = self
        # Das Codewort ist zunächst noch leer und wird
        # von rechts gefüllt, da wir den Baum
        # von unten nach oben abgehen.
        code = ""
        # Wir nutzen eine Schleife, um alle Knoten
        # durchzugehen, bis wir an der Wurzel sind.
        while currentNode is not None:
            # Wenn der Knoten linkes Kind ist, hänge links
            # vom Codewort eine Null an, wenn er rechtes
            # Kind ist eine Eins.
            if currentNode.isLeftChild():
                code = "0" + code
            elif currentNode.isRightChild():
                code = "1" + code
            # Danach wird der Elternknoten betrachtet und
            # der Vorgang wiederholt.
            currentNode = currentNode.parent
        return code
    
    
    # Hier ist die Methode für die Latex-Ausgabe.
    def printAsLatex(self):
        # gibt Latex Syntax auf der Konsole aus
        # und benutzt dazu zwei rekursive Hilfsmethoden.
        # '\b' ist reserviert und muss maskiert werden.
        print("\\begin{itemize}")
        self.latexItem()
        print("\end{itemize}")
        print("\Tree " + self.latexTree())
        
    # Die beiden eben erwähnten Hilfsmethoden:
    
    # Hier werden die Codewörter aller
    # Elementarereignisse in einer Latex-Auflistung
    # ausgegeben.
    def latexItem(self):
        """Besucht alle Kindknoten des Baumes und führt
        eine Operation auf ihnen aus"""
        # Wenn der Knoten einen nicht leeren Schlüssel hat,
        # ist er ein Blatt, dann gib das Codewort zurück.
        if self.key is not None:
            print ("\item Code für '" + self.key + "': " + self.getCode())
        # Wenn er einen linken bzw rechten Kinderknoten hat,
        # wird diese Funktion auf diesem Kinderknoten
        # ausgeführt.
        # Durch diese Rekursion werden die Blätter von
        # links nach rechts abgetastet. (Streng genommen
        # wird der komplette Baum der Tiefe nach
        # durchlaufen, eine Ausgabe erfolgt jedoch nur
        # in den Blättern.) Die Tiefe der
        # Verkettungen ist dann immer die Tiefe des Baumes.
        if self.leftChild is not None:
            self.leftChild.latexItem()
        if self.rightChild is not None:
            self.rightChild.latexItem()
    # Hier wird ein Baum im Latex Syntax ausgegeben:
    def latexTree(self):
        # Wir beginnen mit einer leeren Liste,
        # an welche entsprechende Latex Schlüsselworte
        # angehängt werden.
        resultList = []
        resultList.append("[.{")
        # Die Schlüsselworte werden samt Häufigkeit
        # notiert. Die Rekursion ist analog zur vorherigen.
        if self.key is not None:
            resultList.append(self.key)
            resultList.append(" (")
        resultList.append(str(self.count))
        if self.key is not None:
            resultList.append(")")
        resultList.append("} ")
        # Führt sich rekursiv auf dem
        # linken Kinderknoten aus.
        if self.leftChild is not None:
            resultList.append(self.leftChild.latexTree())
        resultList.append(" ")
        # Führt sich rekursiv auf dem
        # rechten Kinderknoten aus.
        if self.rightChild is not None:
            resultList.append(self.rightChild.latexTree())
        resultList.append("]")
        return ''.join(resultList)


# Die Nachricht, für die ein
# Huffman-Code erstellt werden soll:
inputString = "abbcccddddeeeee"

# Zuerst müssen wir die Häufigkeiten
# der Elementarereignisse ermitteln.
# (Beginn Schritt 1)
# Wir benutzen dafür ein Dictionary.
countDict = {}

# Ein Dictionary ist Menge von Tupeln
# und in jedem Tupel wollen wir
# ein Elementarereignis samt seiner
# Häufigkeit speichern,
# z.B. ('c', 3).

# Den Zählvorgang realisieren wir
# mit Hilfe einer Schleife.

for c in inputString:
    # Für jeden Buchstaben c aus der Nachricht
    # holen wir die Häufigkeit aus dem Dictionary
    # und speichern sie in der Zählvariablen 'count',
    # wenn c nicht im Dictionary enthalten ist,
    # initialisieren wir 'count' mit 0.
    count = countDict.get(c, 0)
    # Wir inkrementieren 'count' um 1.
    count = count + 1
    # Danach schreiben wir die neue Häufigkeit
    # wieder zurück in das Dictionary.
    countDict[c] = count


# Jetzt befinden sich die Häufigkeiten für jedes
# Element der Nachricht in einer indizierten
# Datenstruktur.

# Wir legen eine leere Liste an.
nodeList = []


# Jetzt erstellen wir aus jedem Element
# des Dictionary einen Knoten und merken
# uns diese in der neuen Liste.

# Wir benutzen wieder eine Schleife,
# die jedes Element des Dictionary durchgeht.

for item in countDict.items():
    # item ist ein Element des Dictionary,
    # also ein Tupel, dessen erster Eintrag
    # das Element der Nachricht und dessen zweiter
    # Eintrag dessen Häufigkeit ist.
    nodeList.append(Node(item[0], item[1]))
    # Wir hängen nun eine Instanz der Knotenklasse
    # an unsere Liste und übergeben die Einträge
    # des Tupels an den Konstruktor.
    
# (Ende des 1. Schrittes)

# Jetzt sortieren wir unsere Knotenliste.
# Wir überschreiben unsere Liste hierfür
# mit einer sortierten Version von sich
# selbst.
# (Beginn Schritt 2)

nodeList = sorted(nodeList, key=lambda x:x.count)
# Die Knotenliste ist jetzt absteigend nach der
# Häufigkeit sortiert.


# Solange mehr als ein Knoten in der Liste ist,
# wird folgende Schleife wiederholt:
while len(nodeList) > 1:
    # Zuerst entnehmen wir die seltensten
    # zwei Knoten (also die, die nach der
    # Sortierung am Anfang der Liste standen)
    # und merken sie uns.
    # Die Liste ist danach auch um zwei
    # Elemente kleiner.
    firstNode = nodeList.pop(0)
    secondNode = nodeList.pop(0)
    
    # Jetzt erstellen wir einen neunen Knoten,
    # im Text oben 'e'. Er bekommt keinen Schlüssel,
    # da es keinem Elementarereignis entspricht.
    # Der Zähler ist die Summe der Zähler der eben
    # entnommenen Knoten. Hierdurch ist der Zähler der
    # Wurzel die Mächtigkeit der Nachricht.
    # (Schritt 3)
    parentNode = Node(None, firstNode.count + secondNode.count)
    
    # Dem neuen Knoten hängen wir nun die beiden
    # entnommenen Knoten an, so dass ein (Teil-)Baum
    # entsteht.
    parentNode.setLeftChild(firstNode)
    parentNode.setRightChild(secondNode)
    
    # Jetzt fügen wir den neuen Knoten wieder in die
    # ursprüngliche Knotenliste ein.
    # (Schritt 4)
    nodeList.append(parentNode)
    
    # Zum Schluss sortieren wir wieder nach Häufigkeit:
    nodeList = sorted(nodeList, key=lambda x:x.count)
# (Schritt 5)
# Wenn die Schleifen abbricht, ist nur
# noch ein Knoten in der Liste
# (siehe Abbruchbedingung).
# Diesen letzten entnehmen wir als Wurzel
# der Knotenliste, welche somit leer ist.
rootNode = nodeList.pop()

# Der Wurzelknoten hat nun alle Knoten des
# Huffman-Baumes als Kinder-, Enkel-, ... Knoten.

# Jetzt lassen wir uns das zugehörige Codebuch
# als Liste und Baum im Latex Syntax ausgeben:
rootNode.printAsLatex()
