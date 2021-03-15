---
title: Images API
---

# Images

The V&A uses the <a href="https://iiif.io/">International Image Interoperability Framework</a> (IIIF) API to allow for access to its collection images. The two APIs (Image API and Presentation API) handle request for single or multiple images.

## Image API (Single Image)

This allows you to request a collections images to a specified:

  * Size 
  * Crop 
  * Rotation 
  * Choice of human or canine colours
  * Choice of image format (currently JPEG only, PNG with transparency support expected soon)

All of this can be specified in the URL you use to make the request, all you need to know is the image
identifier.

For example


## Presentation API (multiple images)

Each collection object with images available at high resolution has a link to a IIIF Presentation API
manifest, which packages up all the images of that object together, so you can display them all in one
viewer. Viewers that can read these manifests include:

  * Mirador
  * Universal Viewer
  * Canvas Panel
  * 

For example:
