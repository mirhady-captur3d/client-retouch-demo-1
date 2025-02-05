import streamlit as st
from streamlit_image_comparison import image_comparison
import cv2

st.set_page_config("Captur3d AI photo retouching alpha - demo test", "🔭", layout="left")


st.markdown("""
    <style>
    .main .block-container {
        max-width: 100% !important;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .center-container {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)


st.header("🔭 Magic retouch")
st.write("")
"A combination of automated color correction tasks and photo upscaling"
st.write("")

def centered_image_comparison(img1, img2, label1, label2, width=1200):

    st.markdown(f'<div class="center-container">', unsafe_allow_html=True)

    # Use columns to create a centered layout
    # left, mid, right = st.columns([1, 10, 5])
    # with mid:
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
