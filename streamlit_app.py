import streamlit as st
from streamlit_image_comparison import image_comparison

st.set_page_config(
    "Captur3d AI photo retouching alpha - demo test", 
    "🔭", 
    layout="wide"  # Changed to wide layout
)

# Custom CSS with proper ordering
st.markdown("""
    <style>
    div[data-testid="column"] {
        text-align:center;
    }
    
    .stImageComparison {
        margin: 0 auto;
    }
    
    /* Adjust these values as needed */
    .stImageComparison > div {
        max-width: 1400px !important;
    }
    </style>
""", unsafe_allow_html=True)


st.header("🔭 Magic retouch")
st.write("")
"A combination of automated color correction tasks and photo upscaling"
st.write("")

def centered_image_comparison(img1, img2, label1, label2, width=1400):

    st.markdown(f'<div class="center-container">', unsafe_allow_html=True)

    # Use columns to create a centered layout
    left, mid, right = st.columns([1, 10, 1])
    with mid:
        image_comparison(
            img1=img1,
            img2=img2,
            label1=label1,
            label2=label2,
            width=width  # 1.5x original width (assuming original was ~600px)
        )

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### test image 1")
centered_image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/1.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/1_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 2")
centered_image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/2.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/2_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 3")
centered_image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/3.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/3_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 4")
centered_image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/4.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/4_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 5")
centered_image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/5.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/5_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 6")
centered_image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/6.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/6_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 7")
centered_image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/7.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/7_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 8")
centered_image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/8.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/8_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 9")
centered_image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/9.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/9_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 10")
centered_image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/10.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/10_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 11")
centered_image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/11.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/11_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 12")
centered_image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/12.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/12_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 13")
centered_image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/13.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/13_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 14")
centered_image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/14.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/14_after.jpg",
    label1="input",
    label2="magic retouch",
)
