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

  * Image classification
  * Image labelling
  * Image captioning
  * Image descriptions

are all considered the same issue, namely the generation of a certain length of text based on an image, and they vary only in the length of text generated.

Some researchers do explicitly focus on an area though, for example generating a full multi paragraph description as opposed to a single sentence caption or generating a grammatically correct sentence (aka a caption) instead of a sentence formed of a series of classes (labelling) i.e. "An etching depicting Hercules fighting centaurs" rather than "etching, centaurs, Hercules". Unfortunately it is not always clear in research though if the same meaning always applies - for some "etching, centaurs, hercules" is considered a caption, not just labelling. For the four problems here we are trying to consistenly define them like so:

  * Image classification - etching
  * Image labels - etching, centaurs, Hercules
  * Image caption - An etching depicting Hercules fighting centaurs
  * Image description - This etching depicts the Ancient Greek demi-god Hercules fighting against three centaurs [...]

## Bibliography 

### Cultural Heritage

#### 2023


  * Martinez Pandiani, D.S. et al. (2023) ‘Hypericons for interpretability: decoding abstract concepts in visual data’, International Journal of Digital Humanities, 5(2–3), pp. 451–490. Available at: https://doi.org/10.1007/s42803-023-00077-8.

#### 2021

  * Cetinic, E. (2021) ‘Towards Generating and Evaluating Iconographic Image Captions of Artworks’, Journal of Imaging, 7(8), p. 123. Available at: https://doi.org/10.3390/jimaging7080123. [

  * Milani, Federico, and Piero Fraternali, ‘A Dataset and a Convolutional Model for Iconography Classification in Paintings’, J. Comput. Cult. Herit., 14.4 (2021), p. 46:1-46:18, doi:10.1145/3458885

## Variations

### Major Variations

  * 8/A - Restrict labelling to that within a particular domain (materials, techniques, place, etc)
  * 8/B - Restrict labelling known to those within a particular domain vocabulary (AAT, TGN, Iconclass)

### Minor Variations

  * 8/a - Output the labels in multiple languages

