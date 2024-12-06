import "./App.css";
import Main from "./components/main";
import Sidebar from "./components/Sidebar";
import { useState } from "react";

function App() {
  const [notes, setNotes] = useState([]);
  const onAddNote = () => {
    console.log("新しくノートが追加されました");
    const newNote = {
      id: 1,
      title: "新しいノートです",
      content: "新しいノートの内容",
      modDate: Date.now(),
    };
    setNotes([...notes, newNote]);
    console.log(notes);
  };
  return (
    <div className="App">
      <Sidebar onAddNote={onAddNote} />
      <Main />
    </div>
  );
}

export default App;
