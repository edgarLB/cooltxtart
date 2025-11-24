import tempImageFull from './assets/full.png'
import tempImageNoBG from './assets/no_bg.png'
import {useState} from "react";

function App() {

    const [useNoBG, setUseNoBG] = useState<boolean>(false)

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
            <div className="box image-box">
                <img src={displayVariant()} alt="Image" className="preview-image"/>
            </div>

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
