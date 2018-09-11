function [ output_args ] = kmeans_segmentation( input_args )
% Segmentation of intestine images using kmeans clustering

    clear all, close all;

    load 'videos/bubbles';

    k=3; % the number k of seeds in the kmeans

    im=bubbles(:,:,:,1);

    im_points=reshape(im,size(im,1)*size(im,2),3);
    [IDX,C] = kmeans(double(im_points),k);

    im_idx=reshape(IDX,size(im,1),size(im,2));
    im_segm_points=C(IDX,:);
    im_segm=reshape(im_segm_points,size(im,1),size(im,2),3);

    subplot(1,3,1), imshow(im), title('Original image'),
    subplot(1,3,2), imshow(uint8(im_idx),[]), title('idx image'),
    subplot(1,3,3), imshow(uint8(im_segm)), title('Segmented image by kmeans');

end

