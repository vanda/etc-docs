# 8. Object Image Labelling

Also known as: multi-label classification, image keywords, image tagging, image labels.

Not to be confused with: multi-class classification (see https://scikit-learn.org/stable/modules/multiclass.html#multiclass-classification )

## Problem

**Problem Statement**

Generate a relevant set of labels to describe the digital image of a cultural heritage object.

**Background**

A fairly obvious problem not specific to cultural heritage, to be able to generate relevant keywords describing the main features of an image. For images of cultural heritage objects this would ideally describe both the cultural heritage object (i.e. "a vase") and the visual content of the cultural heritage object (i.e. "a vase with acanthus leaf carving, is thought to show Odysseus, Agamemnon and Iphigenia"). It would be near impossible for it to give any other information not directly obtainable from the image alone, such as the provenance of the object or the exact place of production (for example generating the text "This Sèvres vase is a copy of the antique " Medici Krater" or ''Medici Vase'' a first-century Greek marble decorated with bas-reliefs, in the Uffizi Gallery, Florence" if only shown an image of this [https://collections.vam.ac.uk/item/O8978/vase-s%C3%A8vres-porcelain-factory/](vase))

**Related Problems**

For much research on this problem the following:

  * 2-image-classification
  * 3-image-labelling
  * 4-image-caption

are all considered the same issue, namely the generation of a certain length of text based on an image, and they vary only in the length of text generated.

Some researchers do explicitly focus on an area though, for example generating a full multi paragraph description as opposed to a single sentence caption or generating a grammatically correct sentence (aka a caption) instead of a sentence formed of a series of classes (labelling) i.e. "An etching depicting Hercules fighting centaurs" rather than "etching, centaurs, Hercules". Unfortunately it is not always clear in research though if the same meaning always applies - for some "etching, centaurs, hercules" is considered a caption, not just labelling. For the four problems here we are trying to consistenly define them like so:

  * Image classification - etching
  * Image labels - etching, centaurs, Hercules
  * Image caption - An etching depicting Hercules fighting centaurs
  * Image description - This etching depicts the Ancient Greek demi-god Hercules fighting against three centaurs [...]

## Bibliography 

### Cultural Heritage

#### 2023

  * Cetinic, E. (2021) ‘Towards Generating and Evaluating Iconographic Image Captions of Artworks’, Journal of Imaging, 7(8), p. 123. Available at: https://doi.org/10.3390/jimaging7080123. [

#### 2021

  * Milani, Federico, and Piero Fraternali, ‘A Dataset and a Convolutional Model for Iconography Classification in Paintings’, J. Comput. Cult. Herit., 14.4 (2021), p. 46:1-46:18, doi:10.1145/3458885

### General

## Solutions

### Leading Approaches

A personal view on those approaches to the challenge that seem to be achieving the greatest success. See X for a discussion on why this is not easy to declare a "winner".

### Publication/Project Tracking

An attempt to keep track of published approaches to this challenge indicating different approaches and architectures over time. Not attempting to be comprehensive but focused on innovations in approach and larger steps forward. See X for a discussion on why it is not easy to rank approaches.

### Sample Implementation

## Variations

### Major Variations

  * 3/A - Restrict labelling to that within a particular domain (materials, techniques, place, etc)
  * 3/B - Restrict labelling known to those within a particular domain vocabulary (AAT, TGN, Iconclass)

### Minor Variations

  * 3/a - Output the labels in multiple languages

### Type Specific Variations

  * 3/1 - Painting Specific keywords
    
## Linkages

  * Keywords can then be used as part of with image classification, retrieval,
  * Keywords can be the base of 

## Projects & Tools

### Cultural Heritage

To be done

### General

To be done

