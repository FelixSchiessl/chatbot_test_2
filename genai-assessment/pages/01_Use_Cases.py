import streamlit as st
import streamlit.components.v1 as components

def main():
    # Page configuration
    st.set_page_config(
        page_title="GenAI Use Cases Explorer",
        page_icon="💡",
        layout="wide"
    )

    # Header
    st.title("💡 Explore GenAI Use Cases")
    st.write(
        "Discover how Generative AI can transform different aspects of your business. "
        "Chat with our AI expert to explore specific use cases for your industry."
    )

    # Industry selector
    industry = st.selectbox(
        "Select your industry",
        ["Healthcare", "Finance", "Retail", "Manufacturing", "Technology", "Education", "Other"]
    )

    # Sample use cases grid
    st.write("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎯 Common Use Cases
        - **Content Generation & Marketing**
            - Marketing copy and campaigns
            - Social media content
            - Product descriptions
        - **Customer Service**
            - 24/7 customer support
            - FAQ automation
            - Ticket classification
        - **Data Analysis**
            - Report generation
            - Data summarization
            - Trend analysis
        """)
    
    with col2:
        st.markdown("""
        ### 🚀 Emerging Applications
        - **Process Automation**
            - Document processing
            - Email management
            - Workflow optimization
        - **Product Development**
            - Feature ideation
            - User feedback analysis
            - Requirements documentation
        - **Knowledge Management**
            - Documentation creation
            - Internal knowledge base
            - Training materials
        """)

    # Feazy Chat Integration
    st.write("---")
    st.subheader("Explore Your Use Cases")
    st.write("Chat with our AI expert to discover the most relevant GenAI applications for your specific needs.")
    
    # Embedding Feazy chat component
    feazy_html = """
    <!DOCTYPE html>
    <html style="height: 100%;">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                margin: 0;
                padding: 0;
                height: 100vh;
                overflow: hidden;
            }
            #chat-container {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                z-index: 1000;
                background: white;
            }
            chat-component {
                --primary-color: #2E86C1;
                --secondary-color: #F8F9F9;
                --text-color: #333333;
                --border-color: #E5E7E9;
                --bot-message-bg: #EBF5FB;
                --user-message-bg: #F4F6F7;
                --header-bg: #2E86C1;
                --header-text: #FFFFFF;
                height: 100%;
                width: 100%;
                display: block;
            }
        </style>
    </head>
    <body>
        <div id="chat-container">
            <script type="module" src="https://unpkg.com/feazy-plugin/dist/feazy-chat-component.es.js"></script>
            <chat-component 
                licensing-key=""
                promptId="28c99f7b-ce8a-4693-8c03-e887962eb1ad"
                isDialogVisible="true">
            </chat-component>
        </div>
    </body>
    </html>
    """
    
    # Using streamlit components to render the Feazy chat
    components.html(feazy_html, height=1000, scrolling=False)

    # Footer
    st.write("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666666; padding: 20px;'>
            Need help? Contact our support team at support@example.com
            <br><br>
            <small>This is a demo application showcasing <a href="https://feazy.de" target="_blank">Feazy</a>'s chat capabilities.</small>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()