class Song:

    def __init__(self, title, artist, duration):
        self.title = title;
        self.artist = artist;
        self.duration = duration;
        self.next = None;
        self.previous = None;

    def showSong(self):
        print("{}\t{}\t{}".format(self.title, self.artist, self.duration))

s1 = Song("1 song", "1 singer", 1.1)
s2 = Song("2 song", "2 singer", 2.1)
s3 = Song("3 song", "3 singer", 3.1)
s4 = Song("4 song", "4 singer", 4.1)
s5 = Song("5 song", "5 singer", 5.1)

s1.next = s2
s2.next = s3
s3.next = s4
s4.next = s5
s5.next = s1

s1.previous = s5
s2.previous = s1
s3.previous = s2
s4.previous = s3
s5.previous = s4

# s1.showSong()
# s1.next.showSong()
# s1.previous.showSong()

# print("s1:", s1)                    # hash codes of memory location
# print("s2:", s2)                    # hash codes of memory location
# print("s3:", s3)                    # hash codes of memory location
# print("s4:", s4)                    # hash codes of memory location
# print("s5:", s5)                    # hash codes of memory location

print(">>Playlist Order: First to Last")

temp = None
temp = s1

while temp.next != s1:
    temp.showSong()
    temp = temp.next

temp.showSong()

print(">>Playlist Order: Last to First")

temp = s5

while temp.previous != s5:
    temp.showSong()
    temp = temp.previous

temp.showSong()