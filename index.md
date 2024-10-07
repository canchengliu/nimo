---
layout: cv
title: Cancheng Liu
email:
  url: mailto:canchengliu@foxmail.com
  text: canchengliu@foxmail.com
phone: +86 17801001934
homepage:
  url: https://scholar.google.com/citations?view_op=list_works&hl=zh-CN&user=2-HpgTYAAAAJ
  text: scholar.google.com
address: Ziroom Apartment, Room 409, 168 Jijiamiao Road, Chaoyang District, Beijing, 100070, China.

---

<!-- # Wode **Liu** -->
# **Cancheng Liu**

<!--
include contact information from the front matter
Supported arguments:
    - homepage: url, text
    - phone
    - email
-->

{% include cv-contact.html %}

## Education

### **Sun Yat-sen University** `2012.9 - 2016.6`

```
GuangZhou, China
```

- Bachelor of Software Engineering
- GPA: 3.5/5

## Publications

### Wang S, **Liu C**, Gao X, et al. **Session-based fraud detection in online e-commerce transactions using recurrent neural networks[C]**//_Machine Learning and Knowledge Discovery in Databases: European Conference, ECML PKDD 2017, Skopje, Macedonia, September 18–22, 2017, Proceedings, Part III 10. Springer International Publishing_, 2017: 241-252. [[PDF](https://people.iiis.tsinghua.edu.cn/~weixu/Krvdro9c/SWang_ECMLPKDD_2017.pdf)]

### Xu G, Song Z, Sun Z, … **Liu C**, et al. **Camel: A weakly supervised learning framework for histopathology image segmentation[C]**//_Proceedings of the IEEE/CVF International Conference on computer vision_. 2019: 10682-10691. [[PDF](http://openaccess.thecvf.com/content_ICCV_2019/papers/Xu_CAMEL_A_Weakly_Supervised_Learning_Framework_for_Histopathology_Image_Segmentation_ICCV_2019_paper.pdf)]

### Song Z, Zou S, Zhou W, … **Liu C**, et al. **Clinically applicable histopathological diagnosis system for gastric cancer detection using deep learning[J]**. _Nature communications_, 2020, 11(1): 4294. [[PDF](https://www.nature.com/articles/s41467-020-18147-8.pdf)]

### Niu Y, **Liu C C**, Zhang B L, et al. **Clinically applicable Gleason grading (GD) system for prostate cancer based on deep learning[J]**. _Chinese Medical Journal_, 2021, 134(7): 859-861. [[PDF](https://journals.lww.com/cmj/_layouts/15/oaks.journals/downloadpdf.aspx?an=00029330-202104050-00019)]

### Ba W, Wang S, **Liu C**, et al. **Histopathological diagnosis system for gastritis using deep learning algorithm[J]**. _Chinese Medical Sciences Journal_, 2021, 36(3): 204-209. [[HTML](https://www.sciencedirect.com/science/article/pii/S1001929421000584)]

### Song Z, Yu C, Zou S, … **Liu C**, et al. **Automatic deep learning-based colorectal adenoma detection system and its similarities with pathologists[J]**. _BMJ open_, 2020, 10(9): e036423. [[PDF](https://bmjopen.bmj.com/content/bmjopen/10/9/e036423.full.pdf)]

### Ba W, Wang S, Shang M, … **Liu C**, et al. **Assessment of deep learning assistance for the pathological diagnosis of gastric cancer[J]**. _Modern Pathology_, 2022, 35(9): 1262-1268. [[HTML](https://www.sciencedirect.com/science/article/pii/S0893395222002824)]

### Pan Y, Sun Z, Wang W, … **Liu C**, et al. **Automatic detection of squamous cell carcinoma metastasis in esophageal lymph nodes using semantic segmentation[J]**. _Clinical and Translational Medicine_, 2020, 10(3): e129. [[PDF](https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/ctm2.129)]

### Li J, Zheng B, Pan Y, … **Liu C**, et al. **Transfer of manual annotation in digital pathological images of colorectal cancer with different scanners[J]**. _Chinese Journal of Colorectal Diseases (Electronic Edition)_, 2020, 9(05): 475. [[HTML](https://icu.cma-cmc.com.cn/EN/abstract/abstract138.shtml)]

## Patents

Applied for and granted 9 Chinese patents, including the _pathology-aided diagnostic system based on artificial intelligence (Publication No. CN109360646A)_, among others.

## Research Experience

**Session-Based Fraud Detection in Online E-Commerce Transactions Using Recurrent Neural Networks (ECML PKDD'17)**<br>
_Data Mining Engineer, JD Finance, Beijing, China_ `Jun/2016 – Sep/2017`

- **Fraud Detection System Design and Implementation:** Design and deployment of CLUE, a deep-learning-based fraud detection system using Recurrent Neural Networks (RNN) for JD.com. The system efficiently captured user behavior through click sequences to identify fraudulent patterns in online transactions.
- **Feature Extraction and Data Preprocessing:** Developed innovative techniques for feature extraction from raw web server logs, focusing on user click sequences. Utilized neural-network-based embeddings such as Item2Vec to represent detailed user behavior, improving the accuracy of fraud detection.
- Addressing Imbalanced Datasets and Concept Drift: Tackled challenges posed by highly imbalanced datasets (fraudulent transactions represent less than 0.1% of the total) and the dynamic nature of fraudulent behaviors (concept drift). Applied undersampling, thresholding, and incremental model updates to improve detection efficiency.

<br>

**CAMEL: A Weakly Supervised Learning Framework for Histopathology Image Segmentation (ICCV'19)**<br>
_Algorithm Engineer, Thorough Image, Beijing, China_ `Aug/2018 – Jul/2019`

- **Weakly Supervised Learning Framework:** Designed and implemented CAMEL, a weakly supervised learning framework that utilizes only image-level labels to automatically generate instance-level and approximate pixel-level annotations, significantly reducing the reliance on labor-intensive pixel-level labeling for cancerous region segmentation in histopathology images.
- **Advanced Label Enrichment Techniques:** Developed and integrated combined Multiple Instance Learning (cMIL) with Max-Max and Max-Min criteria, alongside cascade data enhancement and image-level constraints, to enrich supervision information. Achieved performance on par with fully supervised methods in both instance-level classification and pixel-level segmentation on benchmark datasets such as CAMELYON16 and a colorectal adenoma dataset.

<br>

**Clinically applicable histopathological diagnosis system for gastric cancer detection using deep learning (Nature communications'20)**<br>
_Algorithm Engineer, Thorough Image, Beijing, China_ `Feb/2019 – Aug/2020`

- **Achieved High Diagnostic Performance:** Developed a deep convolutional neural network, trained with 2,123 pixel-level annotated H&E-stained whole slide images (WSIs) to accurately detect gastric cancer. Attained over 99% sensitivity and an average specificity of 80.6% on a real-world test dataset of 3,212 WSIs from three different digital scanners, ensuring robust performance across diverse imaging equipment.
- **Conducted Multicenter Validation:** Executed extensive multicenter testing using 1,582 WSIs from two additional medical centers, confirming the system’s consistency and reliability in varied clinical environments.
- Enhanced Diagnostic Accuracy and Clinical Utility: Demonstrated that the AI assistance system significantly improved pathologists’ diagnostic accuracy and reduced misdiagnoses during trial deployments, highlighting its potential for integration into routine clinical practice to alleviate pathologist workload and enhance patient outcomes.

## Work Experience

### **China International Capital Corporation Limited (CICC) - Intelligent Platform** `Jul/2022 – Present`

_Algorithm Engineer_<br>

- **Fine-tuning Vertical Domain Large Models:** Constructed task-specific datasets and fine-tuned large models to enhance their application in the financial sector.
  - Developed a review instruction Q&A dataset covering various document error types, fine-tuned a document review model, created an intelligent review system, and deployed it to the Shanghai, Shenzhen, and Beijing Stock Exchanges. This significantly reduced manual review costs and minimized potential losses and negative public opinion from human errors.
  - Fine-tuned multimodal models to improve the accuracy of extracting structured information from non-standardized documents and receipts.
- **LLMOps Platform Development and Application:** Developed a platform covering the entire lifecycle of large model applications. Utilized large models and cutting-edge technologies to create intelligent applications, promoting business process automation across departments and enhancing information processing speed and decision-making efficiency.
  - Led the design and implementation of core platform functions, integrated internal systems with multi-source data, and guided IT and business teams in developing applications to meet specific requirements.
  - Designed and optimized applications for complex business scenarios using technologies such as RAG (Retrieval-Augmented Generation), CoT (Chain of Thought), Workflow, and Agent.

<br>

### **Thorough Image** `Dec 2017 – Jun 2022`

_Algorithm Engineer_<br>

- **Model Development and Inference Framework:** Developed a framework for whole-slide pathological images (WSIs) to accelerate the development and iteration of multi-organ disease identification models.
  - Designed and built an architecture offering scalable data management, flexible data processing pipelines, modular model architectures, distributed inference support, and comprehensive evaluation tools.
  - Led the development and continuous optimization of the project, maintaining a flexible and stable model development pipeline.
- **Collaborative Research:** Worked with pathology departments of multiple hospitals to develop a multi-organ, multi-disease, multi-task pathological image-assisted diagnosis model library. Integrated it into diagnostic assistance systems and applied it in hospitals, summarizing research results for academic publications.
  - Managed data collection, annotation scheme design, and data processing under the guidance of department heads and physicians.
  - Collaborated closely with physicians to design model architectures and experimental protocols based on the characteristics of different organs and diseases, conducting model training and optimization.
  - Conducted experimental research, organized project findings, and co-authored papers published in journals such as Nature Communications in 2020.
  - Partnered with the product development team to drive the clinical translation and application of technological achievements.

<br>

### **Institute of Data Science, Tsinghua University** `Sep/2017 – Dec/2017`

_Algorithm Engineer_<br>

- **Table Detection and Recognition System:** Developed and trained efficient table detection and recognition models to accurately extract structured information from various document formats, supporting downstream data analysis and information retrieval applications.
  - Expanded and enhanced the training dataset by using PyLaTeX to automatically generate diverse and annotated table data.
  - Trained and optimized various detection and recognition models, achieving high-precision table structure recognition and content extraction.

<br>

### **JD Finance - Risk Management Department** `Jun/2016 – Sep/2017`

_Data Mining Engineer_<br>

- **Fraud Detection Based on User Browsing Behavior:** Developed a real-time fraud detection system that accurately identified and prevented fraudulent transactions by analyzing user browsing behavior sequences. Research results were published at the ECML PKDD 2017 conference.
- **Fraud Detection Based on Relational Networks:** Built a relational network with various node types based on user information and browsing behavior. Implemented graph-related algorithms using Spark GraphX to identify potential risk users by tracing blacklisted users and flagging graylisted ones.

<br>

### **Alibaba - YunOS** `Jul/2015 – Aug/2015`

_Data Mining Engineer (Intern)_<br>

- **Recommendation System:** Developed app recommendations based on community discovery algorithms.

## Skills
**Programming Languages:** Python, C++, Scala <br>
**AI Frameworks:** PyTorch, TensorFlow, DeepSpeed, Accelerate <br>
**Algorithms:** CNN, RNN, Transformers, CLIP, Generative Models <br>
**Big Data:** Frameworks (Spark, Hadoop, Hive), Middlewares (Kafka), Storages (NoSQL Databases, S3), ETL <br>
**DevOps:** Docker, Kubernetes, Jenkins <br>


<!-- ### Footer

Last updated: May 2013 -->
