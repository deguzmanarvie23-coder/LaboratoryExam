

class song:
    def __init__(self, song_id, title, artist, duration):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.duration = duration


class Node:
    def __init__(self, song):
        self.song = song
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return self.head is None

    def insertFirst(self, song):
        new_node = Node(song)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def insertLast(self, song):
        new_node = Node(song)

        if self.isEmpty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self.count += 1

    def insertAt(self, song, position):
        if position <= 0:
            self.insertFirst(song)
            return

        if position >= self.count:
            self.insertLast(song)
            return

        new_node = Node(song)
        current = self.head
        for i in range(position - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.count += 1

    def search(self, song_id):
        current = self.head
        while current is not None:
            if current.song.song_id == song_id:
                return current
            current = current.next
        return None

    def delete(self, song_id):
        if self.isEmpty():
            return False

        if self.head.song.song_id == song_id:
            self.head = self.head.next
            self.count -= 1
            return True

        current = self.head
        while current.next is not None:
            if current.next.song.song_id == song_id:
                current.next = current.next.next
                self.count -= 1
                return True
            current = current.next

        return False

    def display(self):
        if self.isEmpty():
            print("The playlist is empty.")
            return

        current = self.head
        while current is not None:
            s = current.song
            print("--------------------------------")
            print(f"Song ID   : {s.song_id}")
            print(f"Title     : {s.title}")
            print(f"Artist    : {s.artist}")
            print(f"Duration  : {s.duration}")
            current = current.next

        print("--------------------------------")
        print(f"Total songs: {self.count}")

    def size(self):
        return self.count


def add_song_beginning(playlist):
    song_id = input("Enter Song ID: ")
    title = input("Enter Song Title: ")
    artist = input("Enter Artist: ")
    duration = input("Enter Duration: ")

    new_song = song(song_id, title, artist, duration)
    playlist.insertFirst(new_song)
    print("Song added at the beginning!")


def add_song_end(playlist):
    song_id = input("Enter Song ID: ")
    title = input("Enter Song Title: ")
    artist = input("Enter Artist: ")
    duration = input("Enter Duration: ")

    new_song = song(song_id, title, artist, duration)
    playlist.insertLast(new_song)
    print("Song added at the end!")


def insert_song_at_position(playlist):
    song_id = input("Enter Song ID: ")
    title = input("Enter Song Title: ")
    artist = input("Enter Artist: ")
    duration = input("Enter Duration: ")
    position = int(input("Enter position (0 = beginning): "))

    new_song = song(song_id, title, artist, duration)
    playlist.insertAt(new_song, position)
    print("Song inserted!")


def display_playlist(playlist):
    playlist.display()


def search_song(playlist):
    song_id = input("Enter Song ID to search: ")
    node = playlist.search(song_id)

    if node is None:
        print("Song not found.")
    else:
        s = node.song
        print("Song Found:")
        print(f"Song ID   : {s.song_id}")
        print(f"Title     : {s.title}")
        print(f"Artist    : {s.artist}")
        print(f"Duration  : {s.duration}")


def remove_song(playlist):
    song_id = input("Enter Song ID to remove: ")
    success = playlist.delete(song_id)

    if success:
        print("Song removed successfully!")
    else:
        print("Song not found.")


def display_playlist_size(playlist):
    print(f"Total songs in playlist: {playlist.size()}")


def main():
    playlist = LinkedList()

    while True:
        print("\n================================")
        print(" MUSIC PLAYLIST MANAGER")
        print("================================")
        print("1. Add Song at Beginning")
        print("2. Add Song at End")
        print("3. Insert Song at Position")
        print("4. Display Playlist")
        print("5. Search Song")
        print("6. Remove Song")
        print("7. Display Playlist Size")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_song_beginning(playlist)
        elif choice == "2":
            add_song_end(playlist)
        elif choice == "3":
            insert_song_at_position(playlist)
        elif choice == "4":
            display_playlist(playlist)
        elif choice == "5":
            search_song(playlist)
        elif choice == "6":
            remove_song(playlist)
        elif choice == "7":
            display_playlist_size(playlist)
        elif choice == "8":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()

