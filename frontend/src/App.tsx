import tempImageFull from './assets/full.png'
import tempImageNoBG from './assets/no_bg.png'
import {useRef, useState} from "react";
import { resizeImage } from "./utils/resizeImage.ts";

function App() {

    const [useNoBG, setUseNoBG] = useState<boolean>(false)
    const [uploadedImg, setUploadedImg] = useState<string | null>(null)
    const fileInputRef = useRef<HTMLInputElement | null>(null)

    const handleImageClick = () => {
        fileInputRef.current?.click();
    }

    const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files?.[0];
        if (!file) return;

        const resizedBlob = await resizeImage(file)

        const url = URL.createObjectURL(file);
        const resizedUrl = URL.createObjectURL(resizedBlob)

        setUploadedImg(url);

    }

    function displayVariant(): string {
        if (useNoBG) return tempImageNoBG;

        return tempImageFull;
    }

  return (
    <div className="layout">
      <header className="header">
          <h1>cooltxt.art</h1>
      </header>
        <main className="content">
            <p>Click Image to Upload</p>
            <div className="box image-box upload-wrapper" onClick={handleImageClick}>
                <img
                    src={uploadedImg ?? displayVariant()}
                    alt="Image"
                    className="preview-image"
                />

                <div className="upload-overlay">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none"
                         stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                         className="lucide lucide-upload-icon lucide-upload">
                        <path d="M12 3v12"/>
                        <path d="m17 8-5-5-5 5"/>
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                    </svg>
                </div>

                <input
                    type="file"
                    accept="image/*"
                    style={{display: 'none'}}
                    ref={fileInputRef}
                    onChange={handleFileChange}
                />


            </div>

            {uploadedImg ? (
                <div className="box option-box split-box">
                    <button className="split-left" onClick={() => setUploadedImg(null)}>
                        X
                    </button>

                    <button className="split-right" onClick={handleImageClick}>
                        Convert
                    </button>
                </div>
            ) : (
                <>
                    <div className="box option-box">
                        <label>
                            <input
                                disabled={true}
                                type="checkbox"/> Detailed
                        </label>
                    </div>

                    <div className="box option-box">
                        <label>
                            <input
                                onClick={() => setUseNoBG(!useNoBG)}
                                type="checkbox"/> Background
                        </label>
                    </div>

                    <div className="box option-box">
                        <label>
                            <input
                                disabled={true}
                                type="checkbox"/> Effects
                        </label>
                    </div>
                </>
            )}



        </main>
        <footer className="footer">
            <ul className="footer-menu">
                <li><a href="/terms" className="footer-link">Github</a></li>
                <li><a href="/terms" className="footer-link">Terms of Use</a></li>
            </ul>
            <p>Copyright © 2025 EdgarLB, All rights reserved.</p>
        </footer>

    </div>
  )
}

export default App
