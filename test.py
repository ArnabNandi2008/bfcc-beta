for i in range(101,230,2) :
    add1 = str(i)
    add2 = str(i+1)
    print(" "*4,"<tr>",sep="")
    print(" "*6,"<td style=\"width: 50%;\">",sep="")
    print(" "*8,"<a target=\"_blank\" href=\"gallery/",add1,".jpg\">",sep="")
    print(" "*10,"<img class=\"gallery\" src=\"gallery/",add1,".jpg\" width=\"600\" height=\"400\">",sep="")
    print(" "*8,"</a>",sep="")
    print(" "*6,"</td>",sep="")
    print(" "*6,"<td style=\"width: 50%;\">",sep="")
    print(" "*8,"<a target=\"_blank\" href=\"gallery/",add2,".jpg\">",sep="")
    print(" "*10,"<img class=\"gallery\" src=\"gallery/",add2,".jpg\" width=\"600\" height=\"400\">",sep="")
    print(" "*8,"</a>",sep="")
    print(" "*6,"</td>",sep="")
    print(" "*4,"</tr>",sep="")
    
#  4  <tr>
#  6  <td style="width: 50%;">
#  8  <a target="_blank" href="gallery/3.jpg">
# 10  <img class="gallery" src="gallery/3.jpg" width="600" height="400">
#  8  </a>
#  6  </td>
#  6  <td style="width: 50%;">
#  8  <a target="_blank" href="gallery/4.jpg">
# 10  <img class="gallery" src="gallery/4.jpg" width="600" height="400">
#  8  </a>
#  6  </td>
#  4  </tr>