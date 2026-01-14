const API_URL = "http://localhost:8000";

export const fetchDevices = async () => {
    const response = await fetch(`${API_URL}/devices/`);
    if (!response.ok) throw new Error("Failed to fetch devices");
    return response.json();
};

export const fetchUsers = async () => {
    const response = await fetch(`${API_URL}/users/`);
    if (!response.ok) throw new Error("Failed to fetch users");
    return response.json();
};

export const fetchMaintenances = async () => {
    const response = await fetch(`${API_URL}/maintenances/`);
    if (!response.ok) throw new Error("Failed to fetch maintenances");
    return response.json();
};
