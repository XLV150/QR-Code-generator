import pyqrcode

link = "https://www.youtube.com/channel/UCzU9ej8tfHDN_nB_0PQ3cGA"  # PUT ANY LINK YOU WANT IN BETWEEN THE INVERTED COMMAS

url = pyqrcode.create(link)    # THESE LAST 2 LINES GENERATE THE QRCODE AS WELL AS NAMING THE FILE
url.png("Myqr.png", scale=6)

