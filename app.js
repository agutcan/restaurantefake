const API_BASE = `${window.location.protocol}//${window.location.host}`;

function fmt(value) {
  return `${Number(value).toFixed(2)} €`;
}

function orderStatusLabel(status) {
  const labels = {
    pending: "Pendiente",
    paid: "Pagado",
  };

  return labels[status] || status;
}

function paymentStatusLabel(status) {
  const labels = {
    approved: "Aprobado",
  };

  return labels[status] || status;
}

function paymentMethodLabel(method) {
  const labels = {
    cash: "Efectivo",
    card: "Tarjeta",
  };

  return labels[method] || method;
}

async function apiGet(path) {
  const response = await fetch(`${API_BASE}${path}`);
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.detail || "Error en la solicitud");
  }
  return data;
}

async function apiPost(path, payload) {
  const response = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.detail || "Error en la solicitud");
  }
  return data;
}

function getSelectedItems(dishes, prefix = "qty-") {
  return dishes
    .map((dish) => {
      const input = document.getElementById(`${prefix}${dish.id}`);
      const quantity = Number.parseInt(input?.value ?? "0", 10);
      return Number.isFinite(quantity) && quantity > 0
        ? { dish_id: dish.id, quantity }
        : null;
    })
    .filter(Boolean);
}

function setMessage(element, message) {
  element.textContent = message;
}

window.RestaurantApp = {
  API_BASE,
  fmt,
  orderStatusLabel,
  paymentStatusLabel,
  paymentMethodLabel,
  apiGet,
  apiPost,
  getSelectedItems,
  setMessage,
};
