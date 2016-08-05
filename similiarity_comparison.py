#!/usr/bin/python
import math, operator
from PIL import Image
from PIL import ImageChops

def image_similarity_vectors_via_numpy(filepath1, filepath2):
    # source: http://www.syntacticbayleaves.com/2008/12/03/determining-image-similarity/
    # may throw: Value Error: matrices are not aligned . 
    import Image
    from numpy import average, linalg, dot
    import sys
    
    image1 = Image.open(filepath1)
    image2 = Image.open(filepath2)
   
    images = [image1, image2]
    vectors = []
    norms = []
    for image in images:
        vector = []
        for pixel_tuple in image.getdata():
            vector.append(average(pixel_tuple))
        vectors.append(vector)
        norms.append(linalg.norm(vector, 2))
    
    a, b = vectors
    a_norm, b_norm = norms
    # ValueError: matrices are not aligned !
    res = 0.0
    try:
        res = dot(a / a_norm, b / b_norm)
    except ValueError:
        res = "incompatible size"
    except IOError:
        res = "file not found"
    return res


if __name__=='__main__':
    import os.path
    import sys

    if len(sys.argv) < 3:
        print "Usage: python similarity_comparison.py source.txt result.txt"
        sys.exit()

    list = open(sys.argv[1])
    output = open(sys.argv[2], "w")
    
    for subdomain in list:
        if len(subdomain) > 2:
            file1 = './chrometest/' + subdomain[:-1] + '.jpg'
            file2 = './firefoxtest/' + subdomain[:-1] + '.jpg'
        
            res = subdomain[:-1] + " " + str(image_similarity_vectors_via_numpy(file1, file2))
            print res
            output.write(res + "\n")
            output.flush();

    output.close()
