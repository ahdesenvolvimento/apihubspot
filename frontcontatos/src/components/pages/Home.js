import styles from "./Home.module.css";
import Input from "../layout/Input";
import SubmitButton from "../layout/SubmitButton";
import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { LocalStorage } from "ttl-localstorage";
import MyModal from "../layout/MyModal";
import Contatos from "../layout/Contatos";
export default function Home() {
  //   const { code } = useParams();
  const [contato, setContato] = useState([]);
  const [message, setMessage] = useState();
  const [titulo, setTitulo] = useState();
  const [show, setShow] = useState(false);
  const [contatos, setContatos] = useState([]);
  const handleClose = () => setShow(false);
  const handleShow = (message, titulo) => {
    setTitulo(titulo);
    setMessage(message);
    setShow(true);
  };

  let navigate = useNavigate();

  let code = window.location.search.split("=");

  useEffect(() => {
    if (!LocalStorage.get("access-token")) {
      if (code[1]) {
        const init = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ code: code[1] }),
        };
        fetch("http://localhost:8000/api/auth/token/2/", init)
          .then((response) => response.json())
          .then((data) => {
            LocalStorage.put("access-token", data.access_token, 1800);
            LocalStorage.put("refresh-token", data.refresh_token);
            // localStorage.setItem("access-token", data.access_token);
            // navigate("/");
          })
          .catch((error) => console.log(error));
      } else {
        const init = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            refresh_token: LocalStorage.get("refresh-token"),
          }),
        };
        fetch("http://localhost:8000/api/auth/token/1/", init)
          .then((response) => response.json())
          .then((data) => {
            LocalStorage.put("access-token", data.access_token, 1800);
            LocalStorage.put("refresh-token", data.refresh_token);
            navigate("/");
          })
          .catch((error) => console.log(error));
      }
    } else {
      const init = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          refresh_token: LocalStorage.get("refresh-token"),
        }),
      };
      fetch("http://localhost:8000/api/auth/token/1/", init)
        .then((response) => response.json())
        .then((data) => {
          LocalStorage.put("access-token", data.access_token, 1800);
          LocalStorage.put("refresh-token", data.refresh_token);
          navigate("/");
        })
        .catch((error) => console.log(error));
    }
  }, []);

  const cadastrarContato = (e) => {
    e.preventDefault();
    const init = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        data: { properties: contato },
        access_token: LocalStorage.get("access-token"),
      }),
    };
    fetch("http://localhost:8000/contatos/create/", init)
      .then((response) => response.json())
      .then((data) => {
        handleShow(data.message, "Sucesso!");
      })
      .catch((error) => console.log(error));
  };
  function listContatos(e) {
    e.preventDefault();
    const init = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        access_token: LocalStorage.get("access-token"),
      }),
    };
    fetch("http://localhost:8000/contatos/", init)
      .then((response) => response.json())
      .then((data) => {
        setContatos(data.contatos);
        handleShow(
          <Contatos data={contatos} deleteContato={deleteContato} />,
          "Listagem de Contatos"
        );
      })
      .catch((error) => console.log(error));
  }
  const handleChange = (e) => {
    setContato({ ...contato, [e.target.name]: e.target.value });
  };

  const deleteContato = (e) => {
    // e.preventDefault()
    const init = {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        access_token: LocalStorage.get("access-token"),
      }),
    };
    fetch("http://localhost:8000/contatos/delete/" + e, init)
      .then((response) => response.json())
      .then((data) => {
        setContatos(data.contatos);
        handleClose();
        alert("Contato deletado!");
      })
      .catch((error) => console.log(error));
  };

  return (
    <>
        <div className={styles.title}>
          <h4>Formulário de contatos</h4>
        </div>
        <form method="POST" action="" onSubmit={cadastrarContato}>
          <Input
            text="E-mail"
            name="email"
            placholder="Insira o e-mail do contato"
            type="email"
            handleOnChange={handleChange}
          />
          <Input
            text="Telefone"
            name="phone"
            placholder="Telefone"
            type="text"
            handleOnChange={handleChange}
          />
          <Input
            text="Data do aniversário"
            name="date_of_birth"
            type="date"
            handleOnChange={handleChange}
          />
          <Input
            text="Peso"
            name="weight"
            placholder="Peso (kg)"
            type="text"
            handleOnChange={handleChange}
          />
          <div className={styles.button}>
            <SubmitButton text="Criar contato" />
            <button
              type="button"
              className="btn btn-primary mx-2"
              onClick={listContatos}
            >
              Listar Contatos
            </button>
          </div>
        </form>
      <MyModal
        show={show}
        handleClose={handleClose}
        message={message}
        title={titulo}
      />
    </>
  );
}
