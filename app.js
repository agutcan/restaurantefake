const API_BASE =
  window.location.protocol === "file:" || !window.location.host
    ? "http://localhost:8001"
    : `${window.location.protocol}//${window.location.host}`;

// Formatea importes en euros con la convención española.
function fmt(value) {
  return new Intl.NumberFormat("es-ES", {
    style: "currency",
    currency: "EUR",
  }).format(Number(value ?? 0));
}

// Convierte fechas ISO del backend a una representación legible para el usuario.
function formatDate(value) {
  return new Intl.DateTimeFormat("es-ES", {
    dateStyle: "medium",
    timeStyle: "short",
  }).format(new Date(value));
}

// Traduce el estado de un pedido a la etiqueta visible en la interfaz.
function orderStatusLabel(status) {
  const labels = {
    pending: "Pendiente",
    paid: "Pagado",
    preparing: "Preparando",
    cancelled: "Cancelado",
  };

  return labels[status] || status;
}

// Devuelve las clases visuales asociadas a cada estado de pedido.
function orderStatusVariant(status) {
  const variants = {
    pending: {
      label: "Pendiente",
      badge: "text-bg-warning",
      card: "order-pending",
      column: "order-column-pending",
    },
    paid: {
      label: "Pagado",
      badge: "text-bg-success",
      card: "order-paid",
      column: "order-column-paid",
    },
    preparing: {
      label: "Preparando",
      badge: "text-bg-info",
      card: "order-preparing",
      column: "order-column-preparing",
    },
    cancelled: {
      label: "Cancelado",
      badge: "text-bg-danger",
      card: "order-cancelled",
      column: "order-column-cancelled",
    },
  };

  return variants[status] || {
    label: status,
    badge: "text-bg-secondary",
    card: "order-neutral",
    column: "order-column-neutral",
  };
}

// Traduce el estado de un pago a texto legible.
function paymentStatusLabel(status) {
  const labels = {
    approved: "Aprobado",
    rejected: "Rechazado",
  };

  return labels[status] || status;
}

// Traduce el método de pago a una etiqueta humana.
function paymentMethodLabel(method) {
  const labels = {
    cash: "Efectivo",
    card: "Tarjeta",
  };

  return labels[method] || method;
}

// Ejecuta una petición GET contra la API de la aplicación.
async function apiGet(path) {
  const response = await fetch(`${API_BASE}${path}`);
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.detail || "Error en la solicitud");
  }
  return data;
}

// Ejecuta una petición POST con JSON y devuelve la respuesta validada.
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

// Lee las cantidades seleccionadas de la carta y devuelve solo los platos elegidos.
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

// Muestra un mensaje de estado reutilizable en cualquier bloque de la UI.
function setMessage(element, message) {
  element.textContent = message;
}

// Restablece los campos de cantidad al valor base tras crear un pedido.
function resetQuantityInputs(dishes, prefix = "qty-") {
  dishes.forEach((dish) => {
    const input = document.getElementById(`${prefix}${dish.id}`);
    if (input) {
      input.value = 0;
    }
  });
}

// Expone utilidades compartidas para todas las pantallas HTML.
window.RestaurantApp = {
  API_BASE,
  fmt,
  formatDate,
  orderStatusLabel,
  orderStatusVariant,
  paymentStatusLabel,
  paymentMethodLabel,
  apiGet,
  apiPost,
  getSelectedItems,
  setMessage,
  resetQuantityInputs,
};
