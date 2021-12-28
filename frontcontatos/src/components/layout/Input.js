export default function Input({
  text,
  name,
  placholder,
  type,
  handleOnChange,
}) {
  return (
    <div className="form-floating mb-3">
      <input
        type={type}
        className="form-control"
        id={name}
        name={name}
        placeholder={placholder}
        onChange={handleOnChange}
      />
      <label htmlFor={name}>{text}</label>
    </div>
  );
}
