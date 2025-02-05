# 2. Object Detection

## Problem

**Problem Statement**

Identify those parts of an image that contains depictions of known "objects" (likely cultural heritage objects) and return bounding boxes 

**Problem Background**

A very common problem to find within an image some "thing". In some cases the "thing" is known in advance and is what is being looked for specifically (e.g. find all guitars depicted in paintings), in others a class of things is looked for (e.g. find all musical instructments depicted in paintings), and in some no particlar "thing" is known and the challenge is to both detect and classifify. The later is handled seperately.

It should be noted that in most cases object detection is also classification, 
but there are some times where it is solely "detection".

**Related** 

  * 3 - Object Classification (object class)
  * 4 - Object Classification (object instance)

## Bibliography

### Cultural Heritage

#### 2024

  * Kim, Y. et al. (2024) ‘Object Detection in Historical Images: Transfer Learning and Pseudo Labelling’, Journal on Computing and Cultural Heritage, 17(4), pp. 1–15. Available at: https://doi.org/10.1145/3699963.

  * Khan, S. and Noord, N. van (2024) ‘Context-Infused Visual Grounding for Art’. arXiv. Available at: https://doi.org/10.48550/arXiv.2410.12369.

  * Bekkouch, I.E.I. (2024) Auxiliary learning & Adversarial training for Medieval Manuscript Studies. phdthesis. Sorbonne Université. Available at: https://theses.hal.science/tel-04555309 (Accessed: 30 January 2025).

  * Yemelianenko, T. et al. (2024) ‘An approach for dataset extension for object detection in artworks using open-vocabulary models’, in Proceedings of the European Conference on Computer Vision (ECCV) Workshops. Milan (Italie), Italy: ECCV. Available at: https://hal.science/hal-04820558 (Accessed: 25 January 2025).

  * Ramos, P. et al. (2024) ‘No Annotations for Object Detection in Art through Stable Diffusion’. arXiv. Available at: https://doi.org/10.48550/arXiv.2412.06286.

  * Meyer, L. et al. (2024) ‘Algorithmic Ways of Seeing: Using Object Detection to Facilitate Art Exploration’, in Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems. New York, NY, USA: Association for Computing Machinery (CHI ’24), pp. 1–18. Available at: https://doi.org/10.1145/3613904.3642157.

  * Giardinetti, M. et al. (2024) ‘The EyCon Dataset: A Visual Corpus of Early Conflict Photography’, Journal of Open Humanities Data, 10(1). Available at: https://doi.org/10.5334/johd.213.

  * Zhao, Z. (2024) ‘Enhancing artistic analysis through deep learning: a graphic art element recognition model based on SSD and FPT’, PeerJ Computer Science, 10, p. e1761. Available at: https://doi.org/10.7717/peerj-cs.1761.

  * Bengamra, S. et al. (2024) ‘A comprehensive survey on object detection in Visual Art: taxonomy and challenge’, Multimedia Tools and Applications, 83(5), p. 14637. Available at: https://doi.org/10.1007/s11042-023-15968-9.

#### 2023

  * Madhu, P. (2023) Concepts to Computational Constructs: Advanced Scene Understanding for Heterogeneous Artworks Using Deep Learning. Friedrich-Alexander-Universitaet. Available at: https://open.fau.de/handle/openfau/23213 (Accessed: 3 February 2025).

  * Aske, K. and Giardinetti, M. (2023) ‘(Mis)Matching Metadata: Improving Accessibility in Digital Visual Archives through the EyCon Project’, J. Comput. Cult. Herit., 16(4), p. 76:1-76:20. Available at: https://doi.org/10.1145/3594726.

  * Vaigh, C.B.E., Clouzot, M. and Nicolle, C. (2023) ‘Towards A Hybrid Approach for Medieval Illuminations Analysis’, in 2023 17th International Conference on Signal-Image Technology & Internet-Based Systems (SITIS). 2023 17th International Conference on Signal-Image Technology & Internet-Based Systems (SITIS), pp. 78–85. Available at: https://doi.org/10.1109/SITIS61268.2023.00021.

  * Ahmad, T. and Schich, M. (2023) ‘Toward cross-domain object detection in artwork images using improved YoloV5 and XGBoosting’, IET Image Processing, 17(8), pp. 2437–2449. Available at: https://doi.org/10.1049/ipr2.12806.

#### 2022

  * Ibrahim, B.I.E. et al. (2022) ‘Few-Shot Object Detection: Application to Medieval Musicological Studies’, Journal of Imaging, 8(2), p. 18. Available at: https://doi.org/10.3390/jimaging8020018.

  * Milani, F., Pinciroli Vago, N.O. and Fraternali, P. (2022) ‘Proposals Generation for Weakly Supervised Object Detection in Artwork Images’, Journal of Imaging, 8(8), p. 215. Available at: https://doi.org/10.3390/jimaging8080215.

#### 2021

  * Sabatelli, M. et al. (2021) ‘Advances in Digital Music Iconography: Benchmarking the detection of musical instruments in unrestricted, non-photorealistic images from the artistic domain’, Digital Humanities Quarterly, 15(1). Available at: https://orbi.uliege.be/handle/2268/258325 (Accessed: 28 September 2024).

#### 2020

  * Marinescu, M.-C., Reshetnikov, A. and López, J.M. (2020) ‘Improving object detection in paintings based on time contexts’, in 2020 International Conference on Data Mining Workshops (ICDMW). 2020 International Conference on Data Mining Workshops (ICDMW), pp. 926–932. Available at: https://doi.org/10.1109/ICDMW51313.2020.00133.


#### 2018

  * Gonthier, N. et al. (2018) ‘Weakly Supervised Object Detection in Artworks’, in. Proceedings of the European Conference on Computer Vision (ECCV) Workshops, pp. 0–0. Available at: https://openaccess.thecvf.com/content_eccv_2018_workshops/w13/html/Gonthier_Weakly_Supervised_Object_Detection_in_Artworks_ECCVW_2018_paper.html (Accessed: 8 September 2024).
  * Smirnov, S. and Eguizabal, A. (2018) ‘Deep learning for object detection in fine-art paintings’, in 2018 Metrology for Archaeology and Cultural Heritage (MetroArchaeo). 2018 Metrology for Archaeology and Cultural Heritage (MetroArchaeo), pp. 45–49. Available at: https://doi.org/10.1109/MetroArchaeo43810.2018.9089828.


#### 2017 

  * Crowley, E. (2017) Visual recognition in art using machine learning. http://purl.org/dc/dcmitype/Text. University of Oxford. Available at: https://ora.ox.ac.uk/objects/uuid:d917f38e-64cb-4b09-9ccf-b081fe68b187 (Accessed: 8 September 2024).

#### 2015

  * Hall, P. et al. (2015) ‘Cross-depiction problem: Recognition and synthesis of photographs and artwork’, Computational Visual Media, 1(2), pp. 91–103. Available at: https://doi.org/10.1007/s41095-015-0017-1.

  * Agapito, L., Bronstein, M.M. and Rother, C. (eds) (2015) In Search of Art. Cham: Springer International Publishing (Lecture Notes in Computer Science). Available at: https://doi.org/10.1007/978-3-319-16178-5.

  * Crowley, E.J. and Zisserman, A. (2015) ‘In Search of Art’, in L. Agapito, M.M. Bronstein, and C. Rother (eds) Computer Vision - ECCV 2014 Workshops. Cham: Springer International Publishing, pp. 54–70. Available at: https://doi.org/10.1007/978-3-319-16178-5_4.

