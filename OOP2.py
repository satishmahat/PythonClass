
class Room:
    length=0.0
    breadth=0.0

    def calculatearea(self):
        print("area of room = ", self.length * self.breadth)


studyroom=Room()
studyroom.length=42
studyroom.breadth=30.8
studyroom.calculatearea()


kitchenroom=Room()
kitchenroom.length=20
kitchenroom.breadth=20
kitchenroom.calculatearea()

print(f"The length is {kitchenroom.length} and the breadth is {kitchenroom.breadth}")

