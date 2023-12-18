import cv2
import streamlit as st



def principal():
	st.title("OpenCV Data App")
	st.subheader("Esse aplicativo web permite integrar processamento de imagens com OpenCV")
	st.text("Streamlit com OpenCV")

	arquivo_imagem = st.file_uploader("Envie Sua Imagem", type=["jpg", "png", "jpeg"])

	
	if not arquivo_imagem:
		return None

	imagem_original = Image.open(arquivo_imagem)
	imagem_original = np.array(imagem_original)	
	

	st.text("Imagem Original")

	st.image(imagem_original)


if __name__ == '__main__':
	principal()