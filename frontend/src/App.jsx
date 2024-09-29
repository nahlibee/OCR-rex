import { useState, useEffect } from "react";
import InfoList from "./InfoList";
import "./App.css";
import InfoForm from "./InfoForm";
import Upload1 from "./ImageUpload1";
import Upload2 from "./ImageUpload2";
function App() {
  const [infos, setInfos] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [currentInfo, setCurrentInfo] = useState({})
  const [isLoading, setIsLoading] = useState(false);
  const [err, setErr] = useState('');

  useEffect(() => {
    fetchInfos()
  }, []);

  const fetchInfos = async () => {
    const response = await fetch("http://127.0.0.1:5000/infos");
    const data = await response.json();
    setInfos(data.infos);
  };

  const closeModal = () => {
    setIsModalOpen(false)
    setCurrentInfo({})
  }

  const openCreateModal = () => {
    if (!isModalOpen) setIsModalOpen(true)
  }

  const openEditModal = (info) => {
    if (isModalOpen) return
    setCurrentInfo(info)
    setIsModalOpen(true)
  }

  const onUpdate = () => {
    closeModal()
    fetchInfos()
  }
  const [selectedFile, setSelectedFile] = useState(null);
  const [darkMode, setDarkMode] = useState(false);

  const handleImageUpload = (event) => {
    setSelectedFile(URL.createObjectURL(event.target.files[0]));
  };

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  // Apply dark or light mode to the body
  useEffect(() => {
    if (darkMode) {
      document.body.setAttribute("data-theme", "dark");
    } else {
      document.body.removeAttribute("data-theme");
    }
  }, [darkMode]);

  const handleClick = async () => {
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:5000/work', {
        method: 'GET',
        headers: {
          Accept: 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
      }

      const result = await response.json();

      console.log('result is: ', JSON.stringify(result, null, 4));

      setData(result);
    } catch (err) {
      setErr(err.message);
    } finally {
      setIsLoading(false);
      fetchInfos()
    }
  };



  return (
    <>
    <div className="container"><div className='upload-section'>
      <Upload1  />
      <Upload2  />
      </div>
    
    <div className="container">
      
      
      <button className="upload-button" onClick={handleClick}>upload</button>

      {isLoading && <h2>Loading...</h2>}
      <InfoList class='table container' infos={infos} updateInfo={openEditModal} updateCallback={onUpdate} />
      
      </div></div>
      {/* Dark mode toggle button */}
      <div style={{ textAlign: "center", marginTop: "20px" }}>
        <button className="upload-button" onClick={toggleDarkMode}>
          Toggle {darkMode ? "Light" : "Dark"} Mode
        </button>
      </div>
      
      
    </>
  );
}

export default App;