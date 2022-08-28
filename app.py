import gradio as gr

transformer_model = "huggingface/google/vit-base-patch16-224"
Instructuction = "Browse the internet to download any unique image"
title="Simple Image classification playground"
description = "Drop an image to classify, then observe how the machine learning model\
               is able to show the percentages for different class predictions made."
article = """
            - Select an image from the examples provided as demo image
            - Click submit button to make Image classification
            - Click clear button to try new Image for classification
          """

# Gradio app design
interface = gr.Interface.load(
            transformer_model,
            title = title,
            description = description,
            article = article,
            allow_flagging = "never",
            theme = "peach",
            live = False,
            examples=["examples-jpg/example_image1.png", 
                      "examples-jpg/example_image2.jpg",
                      "examples-jpg/example_image3.jpg"]
            )
interface.launch()