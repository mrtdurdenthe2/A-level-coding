"""
class MediaFile2():
    def setDuration(self, duration):
        self.durartion1 = duration
    def setTitle(self, title):
        self.title1 = title   
    def play(self, title, duration):
        print(f"Playing file {str(title)} with duration {duration} mins.")
    class MusicFile:
        def set(self, name):
            self.name = name
        def play(self):
            print(f"playing song")
    class VideoFile:
        def setQuality(self, quality):
            self.quality = quality



class1 = MediaFile2()
##########################################

class MediaFile:
    def __init__(self):
        self.title = ""
        self.duration = 0

    def setTitle(self, title):
        self.title = title

    def setDuration(self, duration):
        self.duration = duration

    def play(self):
        print(f"Playing file {self.title} with duration {self.duration} mins")

class MusicFile(MediaFile):
    def __init__(self):
        super().__init__()

class VideoFile(MediaFile):
    def __init__(self):
        super().__init__()

music = MusicFile()
music.setTitle("My Favorite Song")
music.setDuration(3)
music.play()

video = VideoFile()
video.setTitle("My Favorite Movie")
video.setDuration(120)
video.play()
"""

class Rectangle:  
  def set(self, length, breadth):    
    self.length=length 
    self.breadth=breadth
  def calArea(self):    
    return self.length*self.breadth
  def calPerimeter(self):
    return 2*(self.length+self.breadth)

class Square(Rectangle):
  def set(self, side):
    super().set(side, side)

class Cube(Square):
    def set(self, lenght):
       self.length=lenght
    def area(self):
      return self.length*self.length*self.length*6
    def volume(self):
      return self.calArea()*6
    

cubeobj = Cube()
cubeobj.length = 5
print(cubeobj.area, cubeobj.volume)
      
      

squareO = Square()
