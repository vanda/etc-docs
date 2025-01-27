# 7. Object Image Classification

## Problem

**Problem Statement**

Generate a keyword classification from a digital image of a cultural heritage object.

**Problem Background**

An obvious issue not specific to cultural heritage, to generate some classification of some kind based on the image features. For images of cultural heritage objects the classification mostly refers to identifying the cultural heritage object itself ('an engraving') but it could also describe the content, the colours, the shape, etc as it is not attached to any specific cataloguing field.

**Related Problems**

For much research on this problem the following:

  * Image classification
  * Image labelling
  * Image captioning
  * Image descriptions

are all considered the same issue, namely the generation of a certain length of text based on an image of a cultural heritage object, and they vary only in the length of text generated.

Some researchers do explictily focus on one area, for example generating a full multi-paragraph description as opposed to a single sentence caption or generating a grammatically correct sentence (aka a caption) instead of a sentence formed of a series of classes (labelling) i.e. "An etching depicting Hercules fighting centaurs" rather than "etching, centaurs, Hercules". It is not always clear in research papers though if the same defintions are being used - for some researchers "etching, centaurs, hercules" is considered a caption not just a set of classes/labels. For the related challenges here they are treated differently (as much as possible) to disinguish the qualitity of results, for example for the same object:

  * Image classification - etching
  * Image labelling/keywords - etching, centaurs, Hercules
  * Image caption - An etching depicting Hercules fighting centaurs
  * Image description - This etching depicts the Ancient Greek demi-god Hercules fighting against...

## Bibliography

### Cultural Heritage

#### 2024

  * Maksimova, E. et al. (2024) ‘Viability of Zero-shot Classification and Search of Historical Photos’, in. CHR 2024: Computational Humanities Research Conference. Available at: https://ceur-ws.org/Vol-3834/paper20.pdf (Accessed: 25 January 2025).

#### 2023

  * Martinez Pandiani, D.S. et al. (2023) ‘Hypericons for interpretability: decoding abstract concepts in visual data’, International Journal of Digital Humanities, 5(2–3), pp. 451–490. Available at: https://doi.org/10.1007/s42803-023-00077-8.


#### 2021

  * Milani, Federico, and Piero Fraternali, ‘A Dataset and a Convolutional Model for Iconography Classification in Paintings’, J. Comput. Cult. Herit., 14.4 (2021), p. 46:1-46:18, doi:10.1145/3458885
  * Sabatelli, M. et al. (2021) ‘Advances in Digital Music Iconography: Benchmarking the detection of musical instruments in unrestricted, non-photorealistic images from the artistic domain’, Digital Humanities Quarterly, 15(1). Available at: https://orbi.uliege.be/handle/2268/258325 (Accessed: 28 September 2024).

### General

## Variations

### Major Variations

  * 7/A - Restrict classification results known to those within a particular vocabulary (AAT, TGN, Iconclass, etc)

### Minor Variations

  * 7/a - Output classification results in multiple languages

