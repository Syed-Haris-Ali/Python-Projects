# pip install stegano
  
from stegano import lsb 

image = "file_path"
mew_img = "flask_hidden.png" # Image Here

msg = 'Your secret message here' #Your Message

# To hide message
lsb.hide(image, message=msg).save(new_img)

# To revel hidden message
message = lsb.reveal(new_img)
print('Hidden message:', message)
