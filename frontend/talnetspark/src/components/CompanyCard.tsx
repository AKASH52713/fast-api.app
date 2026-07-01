import type { company } from "../types/company";
import { useState } from "react";

type Props = {
  companies: company[];
  onedit: (company: company) => void;
  ondelete: (company: company) => void;
  onadd: (company: company) => void;
};

function CompanyCard({
  companies,
  onadd,
  onedit,
  ondelete,
}: Props) {
  const [editingCompanyId, setEditingCompanyId] = useState<number | null>(null);

  const [addform, setAddform] = useState<company>({
    id: 0,
    name: "",
    email: "",
    phone: "",
    location: "",
    jobs: [],
  });

  const [editform, setEditform] = useState<company>({
    id: 0,
    name: "",
    email: "",
    phone: "",
    location: "",
    jobs: [],
  });

  const handleAdd = () => {
    onadd(addform);

    setAddform({
      id: 0,
      name: "",
      email: "",
      phone: "",
      location: "",
      jobs: [],
    });
  };

  const handleEdit = () => {
    onedit(editform);
    setEditingCompanyId(null);
  };

  return (
    <div>
      <h2>Add Company</h2>

      <input
        type="text"
        placeholder="Name"
        value={addform.name}
        onChange={(e) =>
          setAddform({ ...addform, name: e.target.value })
        }
      />

      <input
        type="email"
        placeholder="Email"
        value={addform.email}
        onChange={(e) =>
          setAddform({ ...addform, email: e.target.value })
        }
      />

      <input
        type="text"
        placeholder="Phone"
        value={addform.phone}
        onChange={(e) =>
          setAddform({ ...addform, phone: e.target.value })
        }
      />

      <input
        type="text"
        placeholder="Location"
        value={addform.location}
        onChange={(e) =>
          setAddform({ ...addform, location: e.target.value })
        }
      />

      <button onClick={handleAdd}>Add Company</button>

      <hr />

      {companies.map((company) => (
        <div key={company.id}>
          {editingCompanyId === company.id ? (
            <>
              <input
                type="text"
                value={editform.name}
                onChange={(e) =>
                  setEditform({
                    ...editform,
                    name: e.target.value,
                  })
                }
              />

              <input
                type="email"
                value={editform.email}
                onChange={(e) =>
                  setEditform({
                    ...editform,
                    email: e.target.value,
                  })
                }
              />

              <input
                type="text"
                value={editform.phone}
                onChange={(e) =>
                  setEditform({
                    ...editform,
                    phone: e.target.value,
                  })
                }
              />

              <input
                type="text"
                value={editform.location}
                onChange={(e) =>
                  setEditform({
                    ...editform,
                    location: e.target.value,
                  })
                }
              />

              <button onClick={handleEdit}>Save</button>

              <button onClick={() => setEditingCompanyId(null)}>
                Cancel
              </button>
            </>
          ) : (
            <>
              <h3>{company.name}</h3>
              <p>Email: {company.email}</p>
              <p>Phone: {company.phone}</p>
              <p>Location: {company.location}</p>

              <button
                onClick={() => {
                  setEditingCompanyId(company.id);
                  setEditform(company);
                }}
              >
                Edit
              </button>

              <button onClick={() => ondelete(company)}>
                Delete
              </button>
            </>
          )}

          <hr />
        </div>
      ))}
    </div>
  );
}

export default CompanyCard;