import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { Link, BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/pages/Home";
import Login from "./components/pages/Login";
import { Container } from "react-bootstrap";

function App() {
  return (
    <div className="">
      <Container>
        <Router>
          <Routes>
            <Route exact path="/" element={<Home />}/>
            <Route path="/login" element={<Login />}/>
          </Routes>
        </Router>
        <Home />
      </Container>
    </div>
  );
}

export default App;
