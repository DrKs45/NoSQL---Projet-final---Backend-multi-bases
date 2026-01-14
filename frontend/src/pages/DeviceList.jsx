import React, { useEffect, useState } from 'react';
import { fetchDevices } from '../api/client';
import { Server, MapPin } from 'lucide-react';

const DeviceList = () => {
    const [devices, setDevices] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchDevices()
            .then(data => {
                setDevices(data);
                setLoading(false);
            })
            .catch(err => {
                console.error(err);
                setLoading(false);
            });
    }, []);

    if (loading) return <div>Loading devices...</div>;

    return (
        <div className="card">
            <h2 style={{ marginBottom: '1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <Server size={24} color="var(--accent)" />
                Device Inventory
            </h2>
            <table className="table">
                <thead>
                    <tr>
                        <th>Hostname</th>
                        <th>IP Address</th>
                        <th>Type</th>
                        <th>Location</th>
                        <th>Serial</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {devices.map(device => (
                        <tr key={device.id}>
                            <td style={{ fontWeight: 600 }}>{device.hostname}</td>
                            <td style={{ fontFamily: 'monospace' }}>{device.ip_statique}</td>
                            <td>
                                <span className="status-badge status-active">{device.device_type}</span>
                            </td>
                            <td style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                                <MapPin size={14} /> {device.location || 'Unknown'}
                            </td>
                            <td style={{ fontSize: '0.875rem', color: 'var(--text-secondary)' }}>
                                {device.serial_number}
                            </td>
                            <td>
                                <span className="status-badge status-active">Online</span>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default DeviceList;
