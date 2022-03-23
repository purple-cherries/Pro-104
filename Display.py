import cv2

img= cv2.imread('solar-system.jpg')

text = 'Sun'
cv2.putText(img, text, (100,90), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 2, color = (0,69,255))
text = 'Mercury'
cv2.putText(img, text, (120,175), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.5, color = (128,128,128))
text = 'Venus'
cv2.putText(img, text, (175,275), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.5, color = (0,140,255))
text = 'Earth'
cv2.putText(img, text, (260,175), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.5, color = (100,200,0))
text = 'Mars'
cv2.putText(img, text, (400,275), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.5, color = (9,200,255))
text = 'Jupiter'
cv2.putText(img, text, (600,105), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.5, color = (42,42,165))
text = 'Saturn'
cv2.putText(img, text, (775,295), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.5, color = (220,245,245))
text = 'Uranus'
cv2.putText(img, text, (950,125), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.5, color = (128,128,0))
text = 'Neptune'
cv2.putText(img, text, (1150,275), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.5, color = (139,0,100))

text = 'The MilkyWay Galaxy'
cv2.putText(img, text, (400,30), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 2, color = (255,255,255))

text = 'Did You Know ?: There are estimated to be 2 - 4 billion galaxies,'
cv2.putText(img, text, (400,380), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.8, color = (255,255,255))
text = ' other than our very own MilkWay, approx. 300 million of are suitable for life!'
cv2.putText(img, text, (400,395), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.8, color = (255,255,255))


cv2.imshow('Our Solar System', img)
cv2.waitKey(0)