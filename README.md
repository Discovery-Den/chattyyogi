# chattyyogi
"A specialized custom Language Learning Model (LLM) knowledge base was meticulously developed to answer yoga-related questions. This innovative solution leverages entirely free, open-source APIs and frameworks, ensuring cost-effectiveness and accessibility. The knowledge base generates answers exclusively from a curated collection of yoga textbooks that have been meticulously inputted into the system, ensuring that the information is both accurate and authoritative.

This solution employs a Retrieval-Augmented Generation (RAG) approach, which enhances the quality and relevance of the responses by integrating a retrieval mechanism with the generative model. A key component of this system is the use of Qdrant’s free tier, which provides a high-performance, scalable vector database. Qdrant specializes in storing and querying vector embeddings, which are numerical representations of text, images, or other data types. These embeddings capture the semantic meaning of the data, enabling efficient and accurate information retrieval.

By utilizing Qdrant's free tier, the solution benefits from a robust infrastructure that supports fast, real-time searches and can handle a large volume of data. This capability is crucial for maintaining the responsiveness and reliability of the knowledge base, especially when dealing with the extensive and nuanced information contained in yoga textbooks. The vector database allows for sophisticated similarity searches, ensuring that the most relevant information is retrieved in response to user queries. Qdrant’s architecture ensures that even with growing data, the system remains scalable and performant, providing a seamless user experience.

For generating the answers, the Hugging Face free Inference API was employed. Hugging Face is a leader in the field of natural language processing (NLP) and offers a wide range of state-of-the-art models for various NLP tasks. Their Inference API provides access to powerful language models, enabling the generation of accurate and contextually appropriate responses. The Hugging Face platform supports a collaborative ecosystem where developers and researchers can share and improve machine learning models, ensuring continuous enhancement and up-to-date solutions.

The user interface was designed using Streamlit, a powerful framework for creating interactive web applications. Streamlit ensures that the information is presented in a clear, accessible, and user-friendly manner, enhancing the overall user experience.

Overall, this comprehensive solution integrates advanced machine learning techniques with high-quality data sources and user-friendly presentation tools to provide a reliable and efficient platform for addressing yoga-related inquiries. The incorporation of Qdrant’s vector database not only enhances the retrieval process but also ensures that the system remains scalable and performant as it grows. Hugging Face and the LLaMA model contribute to the precision and relevance of the generated answers, making this knowledge base a robust tool for users seeking information on yoga.

Below few screenshot of application 

## Welcome Page, Who are you?
!["Welcome Page, Who are you?"](container/llm/resource/img/img_1.png)

## Recommend Asanas

!["Recommend Asanas?"](container/llm/resource/img/img_2.png)

## Error Handling

!["Error Handling"](container/llm/resource/img/img.png)