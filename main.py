from pdf2image import convert_from_path
from pytesseract import image_to_string
# from PIL import Image



def convert_pdf_to_img(pdf_file):
    return convert_from_path(pdf_file)


def convert_image_to_text(file):
    text = image_to_string(file)
    return text


def get_text_from_any_pdf(pdf_file):

    images = convert_pdf_to_img(pdf_file)
    

    

    final_text = ""

    for pg, img in enumerate(images):
        # img.show()
        # cv2.imwrite("img.jpg", img)
        img.save("img.jpg")
        print(img.size)
        width,hight=img.size
        
        # print(width,hight)
        x=int(width*0.92)
        img = img.crop((x, 0, width, hight))
        # crop (left, upper, right, lower)
        final_text += convert_image_to_text(img)
        
        with open("out2.txt",'w') as f:
            f.write(final_text)
            f.write('\n')
    return final_text

if __name__=="__main__":
    path_to_pdf = './Structural (1)/S-1.2-PARTIAL-2nd-FLOOR-FRAMINC-PLAN-Rev.0.pdf'

    get_text_from_any_pdf(path_to_pdf)
