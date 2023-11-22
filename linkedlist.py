class LinkedList:
    
    def __init__(self):
        self.myList = []

    
    def get(self, index: int) -> int:
        myList = self.myList

        if index >= 0 and index < len(myList):
            return self.myList[index]
        else:
            return -1

    def insertHead(self, val: int) -> None:
        self.myList.insert(0, val)
        

    def insertTail(self, val: int) -> None:
        myList = self.myList
        myList.insert(len(myList), val)

    def remove(self, index: int) -> bool:
        myList = self.myList
        if index >= 0 and index < len(myList):
            myList.pop(index)
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        return self.myList
