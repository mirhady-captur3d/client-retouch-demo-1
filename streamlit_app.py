import streamlit as st
from streamlit_image_comparison import image_comparison
import cv2


st.set_page_config("Captur3d AI photo retouching alpha - demo test", "🔭", layout="centered")


st.header("🔭 Magic retouch")

st.write("")
"A combination of automated color correction tasks and photo upscaling"
st.write("")

st.markdown("### test image 1")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/1.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/1_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 2")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/2.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/2_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 3")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/3.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/3_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 4")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/4.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/4_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 5")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/5.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/5_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 6")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/6.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/6_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 7")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/7.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/7_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 8")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/8.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/8_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 9")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/9.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/9_after.jpg",
    label1="input",
    label2="magic retouch",
)

st.markdown("### test image 10")
image_comparison(
    img1="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/10.jpg",
    img2="https://automated-photo-retouching-test.s3.ap-southeast-2.amazonaws.com/client/10_after.jpg",
    label1="input",
    label2="magic retouch",
)
