import streamlit as st
import matplotlib.pyplot as plt

def mm1_queue(arrival_rate, service_rate):
    if arrival_rate >= service_rate:
        return None
    
    utilization = arrival_rate / service_rate
    Wq = arrival_rate / (service_rate * (service_rate - arrival_rate))
    Lq = (arrival_rate ** 2) / (service_rate * (service_rate - arrival_rate))
    
    return utilization, Wq, Lq


st.title("Supermarket Checkout Queue Model")
st.write("M/M/1 Queue Simulation")

arrival_rate = st.number_input("Arrival Rate (customers/hour)", min_value=1, value=8)
service_rate = st.number_input("Service Rate (customers/hour)", min_value=1, value=12)

if st.button("Calculate"):

    result = mm1_queue(arrival_rate, service_rate)

    if result is None:
        st.error("System Unstable! Arrival rate must be less than service rate.")
    else:
        utilization, Wq, Lq = result

        st.subheader("Results")
        st.write("Utilization:", round(utilization, 3))
        st.write("Average Waiting Time:", round(Wq * 60, 2), "minutes")
        st.write("Average Customers in Queue:", round(Lq, 3))

        # Graph 1
        arrival_list = []
        waiting_list = []

        for rate in range(1, service_rate):
            r = mm1_queue(rate, service_rate)
            if r:
                arrival_list.append(rate)
                waiting_list.append(r[1] * 60)

        fig1, ax1 = plt.subplots()
        ax1.plot(arrival_list, waiting_list, marker='o')
        ax1.set_xlabel("Arrival Rate")
        ax1.set_ylabel("Waiting Time (minutes)")
        ax1.set_title("Arrival Rate vs Waiting Time")
        ax1.grid(True)

        st.pyplot(fig1)

        # Graph 2
        service_list = []
        waiting_service = []

        for rate in range(arrival_rate + 1, arrival_rate + 15):
            r = mm1_queue(arrival_rate, rate)
            if r:
                service_list.append(rate)
                waiting_service.append(r[1] * 60)

        fig2, ax2 = plt.subplots()
        ax2.plot(service_list, waiting_service, marker='o')
        ax2.set_xlabel("Service Rate")
        ax2.set_ylabel("Waiting Time (minutes)")
        ax2.set_title("Service Rate vs Waiting Time")
        ax2.grid(True)

        st.pyplot(fig2)