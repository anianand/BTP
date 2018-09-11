I = imread('050.png');
gray = rgb2gray(I);
gray = histeq(gray);
level = graythresh(gray);
BW = imbinarize(gray,level);  %otsu Binarisation image should be here 
tam = size(I);
sizex = tam(1);
sizey = tam(2);
output = I;
for i=1:sizex
    for j=1:sizey
        if BW(i,j)==0
            output(i,j,1)=255;
            output(i,j,2)=255;
            output(i,j,3)=255;
        end
    end
end
r=0;
g=0;
b=0;
for i=1:sizex
    for j=1:sizey
        if (output(i,j,1)==255 & output(i,j,2)==255 & output(i,j,3)==255)
            continue
        else
            r=r+output(i,j,1);
            g=g+output(i,j,2);
            b=b+output(i,j,3);
        end
    end
end
r=r/(sizex*sizey);
g=g/(sizex*sizey);
b=b/(sizex*sizey);
for i=1:sizex
    for j=1:sizey
        if BW(i,j)==0
            output(i,j,1)=r;
            output(i,j,2)=g;
            output(i,j,3)=b;
        end
    end
end
gray = rgb2gray(output);
gray = histeq(gray);
level = graythresh(gray);
BW = imbinarize(gray,level);
for i=1:sizex
    for j=1:sizey
        if BW(i,j)==0
            output(i,j,1)=255;
            output(i,j,2)=255;
            output(i,j,3)=255;
        end
    end
end
figure
imshow(output)