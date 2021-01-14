import { gql, useMutation } from '@apollo/client';
import withTheme from "../../withTheme";

const CREATE_RESTURANT = gql`
  mutation ($name: String!) {
    createResturant(name: $name) {
      resturant {
        id
        name
        address
        rating
        price
        phoneNumber
        website
    }
  }
}`;

function CreateResturant() {
  let input;
  const [createResturant, {data}] = useMutation(CREATE_RESTURANT);

    return (
      <div>
        <form
          onSubmit={e => {
            e.preventDefault();
            createResturant({ variables: { name: input.value } });
            input.value = '';
          }}
        >
          <input
            ref={node => {
              input = node;
            }}
          />
          <button type="submit">Add New Resturant</button>
        </form>
      </div>
    );
  }

  export default withTheme(CreateResturant);