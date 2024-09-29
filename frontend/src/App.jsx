import { useState, useEffect } from "react";
import InfoList from "./InfoList";
import "./App.css";
import InfoForm from "./InfoForm";
import Upload from "./ImageUpload";
function App() {
  const [infos, setInfos] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [currentInfo, setCurrentInfo] = useState({})

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

  return (
    <>
    <div className="container">
      <Upload  />
      <InfoList class='table container' infos={infos} updateInfo={openEditModal} updateCallback={onUpdate} />
      
      </div>
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