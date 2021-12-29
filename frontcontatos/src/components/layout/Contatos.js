export default function Contatos({ data, deleteContato }) {
  return (
    <div className="table-responsive">
      <table className="table">
        <thead>
          <tr>
            <th>E-mail</th>
            <th>Telefone</th>
            <th>Data de nascimento</th>
            <th>Peso (kg)</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          {data.map((contato) => (
            <tr key={contato.id}>
              <td>{contato.properties.email}</td>
              <td>{contato.properties.phone}</td>
              <td>{contato.properties.date_of_birth}</td>
              <td>{contato.properties.weight}</td>
              <td>
                <button onClick={(e) => deleteContato(contato.id)} type="button" className="btn btn-danger">
                  Excluir
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
