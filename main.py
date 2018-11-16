
# accessToken = "EAAE0emcSjnEBAFRtZAer36BjZAfFtbQlrqMAArsDaEmQr1qgGACZBfjRnyZAgTZB2sOxzGULuqhOihc3NvaZAJ0L7eqAPWzO8hs3muwQr1xZB3OuEFo6SOPnYpvyUU7UDiwv31ZAtarDZABiZAazOo3kCH0zEDSlToGQPDTcQnN3SOBvfm2MCRjRiVwR7Aupz8uTTuZAxvaWlZArkfFu5p60vn6s"

from PIL import Image
import numpy as np

im = Image.open('data/utkatasana_00.jpg')
im = im.resize((32, 32))
im.save('utkatasana_00_32x32.jpg')
