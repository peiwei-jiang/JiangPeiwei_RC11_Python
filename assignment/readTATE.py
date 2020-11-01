import csv
import requests
from PIL import Image
from io import BytesIO

class ArtTate:
    def __init__(self, id, title, width, depth, height, imageUrl, artist):
        self.id = id
        self.title = title
        self.width = width
        self.depth = depth
        self.height = height
        self.imageUrl = imageUrl
        self.artist = artist
        self.imagePath = ''

        if self.width:
            self.width
        else:
            self.width = 0

        if self.height:
            self.height
        else:
            self.height = 0

        if self.depth:
            self.depth
        else:
            self.depth = 0

    def describe(self):
        print("artist:" + self.artist, "id:" + self.id, "title:" + self.title, "width:" + str(self.width), "depth:" + str(self.depth),"height:" + str(self.height))

    def getImageFile(self):
        if self.imageUrl:
            response = requests.get(self.imageUrl)
            try:
                im = Image.open(BytesIO(response.content))
            except OSError:
                return None
            path = "ArtImageRepository/" + self.artist + "_" + self.id + ".jpg"
            self.imagePath = path
            im.save(path,"JPEG")

artPieces = []
with open("CSVFiles\Artwork_data.csv",encoding='utf-8-sig')as artFile:
    artReader = csv.DictReader(artFile)

    for row in artReader:
        id = row['id']
        title = row['title']
        width = row['width']
        depth = row['depth']
        height = row['height']
        imageUrl = row['thumbnailUrl']
        artist = row['artist']
        if width or depth or height:
            artPiece = ArtTate(id, title, width, depth, height, imageUrl, artist)
            artPieces.append(artPiece)
'''
artPieces["name of artist"].describe()
'''
for art in artPieces:
    if "Monet" in art.artist:
        art.getImageFile()


'''keywords
('id', 'accession_number', 'artist', 'artistRole', 'artistId', 'title',
'dateText', 'medium', 'creditLine', 'year', 'acquisitionYear', 'dimensions', 'width', 'height', 'depth',
'units', 'inscription', 'thumbnailCopyright', 'thumbnailUrl', 'url')

('id', '1035'), ('accession_number', 'A00001'), ('artist', 'Blake, Robert'), ('artistRole', 'artist'),
('artistId', '38'), ('title', 'A Figure Bowing before a Seated Old Man with his Arm Outstretched in Benediction. Verso: Indecipherable Sketch'),
('dateText', 'date not known'),
('medium', 'Watercolour, ink, chalk and graphite on paper. Verso: graphite on paper'),
('creditLine', 'Presented by Mrs John Richmond 1922'), ('year', ''), ('acquisitionYear', '1922'),
('dimensions', 'support: 394 x 419 mm'),
('width', '394'), ('height', '419'), ('depth', ''),
('units', 'mm'), ('inscription', ''), ('thumbnailCopyright', ''),
('thumbnailUrl', 'http://www.tate.org.uk/art/images/work/A/A00/A00001_8.jpg'),
('url', 'http://www.tate.org.uk/art/artworks/blake-a-figure-bowing-before-a-seated-old-man-with-his-arm-outstretched-in-benediction-a00001')'''
