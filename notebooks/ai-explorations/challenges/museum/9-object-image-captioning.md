# 9. Object Image Captioning 

## Problem

**Problem Statement**

Generate a one sentance summary description of an image of a cultural heritage object that could be used as a caption/credit for the image.

**Problem Background**

A fairly obvious problem not specific to cultural heritage, to be able to generate relevant keywords describing the main features of an image. For images of cultural heritage objects this would ideally describe both the cultural heritage object (i.e. "a vase") and the visual content of the cultural heritage object (i.e. "a vase with acanthus leaf carving, is thought to show Odysseus, Agamemnon and Iphigenia"). It would be near impossible for it to give any other information not directly obtainable from the image alone, such as the provenance of the object or the exact place of production (for example generating the text "This Sèvres vase is a copy of the antique " Medici Krater" or ''Medici Vase'' a first-century Greek marble decorated with bas-reliefs, in the Uffizi Gallery, Florence" if only shown an image of this [https://collections.vam.ac.uk/item/O8978/vase-s%C3%A8vres-porcelain-factory/](vase)). Some multi-model approaches to this problem bring in other information alongside image features to enable this richer caption.

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

#### 2024

  * Castellano, G. et al. (2024) ‘Exploring the Synergy Between Vision-Language Pretraining and ChatGPT for Artwork Captioning: A Preliminary Study’, in G.L. Foresti, A. Fusiello, and E. Hancock (eds) Image Analysis and Processing - ICIAP 2023 Workshops. Cham: Springer Nature Switzerland, pp. 309–321. Available at: https://doi.org/10.1007/978-3-031-51026-7_27.
    
#### 2023

  * Cioni, D. et al. (2023) ‘Diffusion Based Augmentation for Captioning and Retrieval in Cultural Heritage’, in. Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 1707–1716. Available at: https://openaccess.thecvf.com/content/ICCV2023W/e-Heritage/html/Cioni_Diffusion_Based_Augmentation_for_Captioning_and_Retrieval_in_Cultural_Heritage_ICCVW_2023_paper.html (Accessed: 23 August 2024).

  * Stefanini, M. et al. (2023) ‘From Show to Tell: A Survey on Deep Learning-Based Image Captioning’, IEEE Transactions on Pattern Analysis and Machine Intelligence, 45(1), pp. 539–559. Available at: https://doi.org/10.1109/TPAMI.2022.3148210.

  * Del Moro, M. et al. (2023) ‘Inception Models for Fashion Image Captioning: An Extensive Study on Multiple Datasets’, in A. Arampatzis et al. (eds) Experimental IR Meets Multilinguality, Multimodality, and Interaction. Cham: Springer Nature Switzerland, pp. 3–14. Available at: https://doi.org/10.1007/978-3-031-42448-9_1.

  * Bongini, P., Becattini, F. and Del Bimbo, A. (2023) ‘Is GPT-3 All You Need for Visual Question Answering in Cultural Heritage?’, in L. Karlinsky, T. Michaeli, and K. Nishino (eds) Computer Vision – ECCV 2022 Workshops. Cham: Springer Nature Switzerland, pp. 268–281. Available at: https://doi.org/10.1007/978-3-031-25056-9_18.

#### 2022

  * Yan, J., Wang, W. and Yu, C. (2022) ‘Affective word embedding in affective explanation generation for fine art paintings’, Pattern Recognition Letters, 161, pp. 24–29. Available at: https://doi.org/10.1016/j.patrec.2022.07.009.
  * Lu, Y. et al. (2022) ‘Data-efficient image captioning of fine art paintings via virtual-real semantic alignment training’, Neurocomputing, 490, pp. 163–180. Available at: https://doi.org/10.1016/j.neucom.2022.01.068.

#### 2021

  * Cetinic, Eva, ‘Towards Generating and Evaluating Iconographic Image Captions of Artworks’, Journal of Imaging, 7.8 (2021), p. 123, doi:10.3390/jimaging7080123
  * Milani, Federico, and Piero Fraternali, ‘A Dataset and a Convolutional Model for Iconography Classification in Paintings’, J. Comput. Cult. Herit., 14.4 (2021), p. 46:1-46:18, doi:10.1145/3458885


### General

#### 2022

  * Sirisha, U. and Sai Chandana, B. (2022) ‘Semantic interdisciplinary evaluation of image captioning models’, Cogent Engineering, 9(1), p. 2104333. Available at: https://doi.org/10.1080/23311916.2022.2104333.

#### 2021

  * Elhagry, A. and Kadaoui, K. (2021) ‘A Thorough Review on Recent Deep Learning Methodologies for Image Captioning’. arXiv. Available at: https://doi.org/10.48550/arXiv.2107.13114.

  * Stefanini, M. et al. (2021) ‘From Show to Tell: A Survey on Deep Learning-based Image Captioning’. arXiv. Available at: https://doi.org/10.48550/arXiv.2107.06912.

#### 2019

  * Hossain, MD.Z. et al. (2019) ‘A Comprehensive Survey of Deep Learning for Image Captioning’, ACM Comput. Surv., 51(6), p. 118:1-118:36. Available at: https://doi.org/10.1145/3295748.

## Variations

### Major Variations

  * 9/A - Provide a caption of the cultural heritage object rather than the digital image - (e.g. a digital image of a watercolour artwork is described as a watercolour)

### Minor Variations

  * 9/a - Output the caption in multiple languages

