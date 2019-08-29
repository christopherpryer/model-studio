select s.id, s.route_id, s.stop_id, s.order_id, s.load_id, s.sku_id,
    s.origin_id, s.origin_city, s.origin_state, s.origin_zip, s.origin_country,
    g1.latitude as origin_lat, g1.longitude as origin_lon,
    s.dest_id, s.dest_city, s.dest_state, s.dest_zip, s.dest_country,
    g2.latitude as dest_lat, g2.longitude as dest_lon,
    s.demand, s.demand_uom
    from shipments as s
        left join geocodes as g1 on (upper(s.origin_city) = upper(g1.city)
            and upper(s.origin_state) = upper(g1.state)
            and upper(s.origin_zip) = upper(g1.zip))
        left join geocodes as g2 on (upper(s.dest_city) = upper(g2.city)
            and upper(s.dest_state) = upper(g2.state)
            and upper(s.dest_zip) = upper(g2.zip))
	order by s.id, s.route_id, s.stop_id;
