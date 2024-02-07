const LabeledCheckbox = ({id, text}) => (
      <React.Fragment>
      <input class="form-check-input" type="checkbox" value="" id={id}/>
      <label class="form-check-label" for={id}>
        {text}
      </label>
      </React.Fragment>
  );
  
  export default LabeledCheckbox;