import streamlit as st
import streamlit.components.v1 as components

def main():
    # Page configuration
    st.set_page_config(
        page_title="GenAI Readiness Assessment",
        page_icon="🤖",
        layout="wide"
    )

    # Main header section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("🤖 GenAI Readiness Assessment")
        st.write(
            "Evaluate your organization's preparedness for implementing Generative AI solutions. "
            "Our assessment will help you understand your strengths and areas for improvement."
        )

    # Assessment overview section
    st.subheader("Assessment Areas")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        ### 📊 Data Readiness
        - Data quality
        - Governance
        - Privacy & security
        """)
    
    with col2:
        st.markdown("""
        ### 💻 Technical Infrastructure
        - Computing resources
        - Integration capabilities
        - Technical expertise
        """)
    
    with col3:
        st.markdown("""
        ### 🎯 Business Strategy
        - Use case identification
        - ROI assessment
        - Implementation planning
        """)
    
    with col4:
        st.markdown("""
        ### 👥 Change Management
        - Organization culture
        - Training programs
        - Process adaptation
        """)

    # Feazy Chat Integration
    st.write("---")
    st.subheader("Start Your Assessment")
    st.write("Chat with our AI expert to assess your organization's GenAI readiness.")
    
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
    
    # Additional Resources Section
    st.write("---")
    st.subheader("Additional Resources")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📚 Learning Resources
        - [Guide to GenAI Implementation](/)
        - [Best Practices & Case Studies](/)
        - [Technical Requirements Guide](/)
        """)
    
    with col2:
        st.markdown("""
        ### 🔗 Useful Links
        - [GenAI ROI Calculator](/)
        - [Implementation Roadmap Template](/)
        - [Training Resources](/)
        """)

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