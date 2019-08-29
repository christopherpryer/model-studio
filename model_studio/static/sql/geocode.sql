select s.id, s.route_id, s.stop_id, s.order_id, s.load_id, s.sku_id,
    s.origin_id, s.origin_city, s.origin_state, s.origin_zip, s.origin_country,
    g1.latitude as origin_lat, g1.longitude as origin_lon,
    s.dest_id, s.dest_city, s.dest_state, s.dest_zip, s.dest_country,
    g2.latitude as dest_lat, g2.longitude as dest_lon,
    s.demand, s.demand_uom
    from shipments as s
        left join geocodes as g1 on (s.origin_city = g1.city
            and s.origin_state = g1.state and s.origin_zip = g1.zip)
        left join geocodes as g2 on (s.dest_city = g2.city
            and s.dest_state = g2.state and s.dest_zip = g2.zip)
	order by s.id, s.route_id, s.stop_id;
